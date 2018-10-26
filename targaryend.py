import sys
import crypt
import itertools
import string

# def guess_password(real):
#     chars = string.ascii_lowercase + string.digits
#     attempts = 0
#     for password_length in range(1, 9):
#         for guess in itertools.product(chars, repeat=password_length):
#             attempts += 1
#             guess = ''.join(guess)
#             if guess == real:
#                 return 'password is {}. found in {} guesses.'.format(guess, attempts)
#             print(guess, attempts)

# print(guess_password('abc'))

printable_str = ""
for i in range(32,127):
	printable_str += chr(i)
print(printable_str)

salt = "aa"
real_hash = ".YVJDT1VruA"

dictionary = []
with open('dictionary.txt', 'r') as f:
	for l in f:
		for w in l.split():
			dictionary.append(w)
print(dictionary)

wordlist = []
with open('words.txt', 'r') as f:
	for l in f:
		for w in l.split():
			wordlist.append(w)
print(wordlist)

for guess in dictionary:
	guess_hash = crypt.crypt(guess, salt)
	if(guess_hash == real_hash):
        print 'password is {}.'.format(guess)
        break
    # print(guess)

for guess in wordlist:
	guess_hash = crypt.crypt(guess, salt)
	if(guess_hash == real_hash):
        print 'password is {}.'.format(guess)
        break
    # print(guess)

for password_length in range(6, 9):
    for guess in itertools.product(printable_str, repeat=password_length):
        guess = ''.join(guess)
        guess_hash = crypt.crypt(guess, salt)
        if(guess_hash == real_hash):
        	print 'password is {}.'.format(guess)
        	break
        # print(guess)
