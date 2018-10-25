
import itertools
import string

printable_str = 'abcdefghij'
for password_length in range(6, 7):
    for guess in itertools.product(printable_str, repeat=password_length):
        guess = ''.join(guess)
        print(guess)
