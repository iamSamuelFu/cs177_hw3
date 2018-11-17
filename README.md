# cs177_hw4
## Samuel Fu

### Task 1:
* By running the executable with GDB, we can dissemble the function authenticate to check the size of the buffer. In this case, the buffer size is 21 bytes in hex. However, we will need a malicious string of 25 bytes (21+4) to overflow the buffer before rewriting the return address because of the EBP addressed stored on top of the stack. After having a 25 bytes of padding, we will examine where we should jump to in order to open the shell, specifically the system call. However, we need to jump to the address line before making the system call because it requires to pass in the string argument `/bin/sh` into the function. Once competed building the malicious string in little endian form, we pass it in to gain shell access.

### Task 2:
* First, we retrieve the shell code from the tutorial and calculate its size in the malicious string. Knowing we have a 45 bytes of shell code to inject and a 4 bytes of return address at the end, we dissemble the function authenticate again with GDB  and find out the buffer size is 0x5c. Therefore, the total size of the string we will need is `92(0x5c) + 4(EBP) + 4(RET) = 100` bytes. Therefore, we need a size of `100 - 45(shell code) - 4(ret) = 51` bytes of NOP sled (filled with 0x90). Now having a 51 bytes of sled, we run the program with GDB again with string `‘0x90’*51 + shell code + random_return address`. Knowing I will get a segmentation fault, I examined the registers around ESP to find where my NOP sled lies in address. Although it is not the same as the actual address in memory due to extra debugging information, it is close enough for us to run trials around it. I picked the middle address of my sled in GDB and started to increment or decrement by 50 bytes around it until I landed on the actual NOP sled and gained shell access.

### Task 3:
* First, by looking at the code, I noticed that we will have really small buffer to overflow. It is too small to fit in the entire shell code, not to mention the return address nor the NOP sled. Therefore, we will use environment variable to store our NOP sled as well as our shell code, then overflow the buffer with the address pointing to somewhere in the middle of the sled to invoke the shell code. Therefore, I set the environment variable SHELLCODE to NOP sled about 500 bytes concatenated with the shell code. Then I run the program with GDB, set break point at the main and examine the register higher than ESP to find where my sled lies in memory as environment variable. Once I see hundreds of register with NOP value `0x90`, I pick the middle address and overflow the buffer with the return address. Fortunately, it helps me gain the shell access on the first try.



