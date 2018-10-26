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
salt = "$1$bAc99821$"
real_hash = "noxC9VXXiMuA0IRfECCVA/"

lowercase_str = string.ascii_lowercase
print(lowercase_str)

printable_str = ""
for i in range(32,127):
    printable_str += chr(i)
print(printable_str)

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

def craker():

    for guess in dictionary:
        guess_hash = crypt.crypt(guess, salt)
        guess_hash = guess_hash[12:]
        if(guess_hash == real_hash):
            print 'password is {} with hash value {}.'.format(guess, guess_hash)
            return
        print 'Guess is {} with hash value {}.'.format(guess, guess_hash)
    print("------------dictionary runs out-----------------")

    for guess in wordlist:
        guess_hash = crypt.crypt(guess, salt)
        guess_hash = guess_hash[12:]
        if(guess_hash == real_hash):
            print 'password is {} with hash value {}.'.format(guess, guess_hash)
            return
        print 'Guess is {} with hash value {}.'.format(guess, guess_hash)
    print("------------wordlist runs out-----------------")

    for password_length in range(6, 9):
        for guess in itertools.product(lowercase_str, repeat=password_length):
            guess = ''.join(guess)
            guess_hash = crypt.crypt(guess, salt)
            guess_hash = guess_hash[12:]
            if(guess_hash == real_hash):
                print 'password is {} with hash value {}.'.format(guess, guess_hash)
                return
            print 'Guess is {} with hash value {}.'.format(guess, guess_hash)
    print("------------lowercase runs out-----------------")

    for password_length in range(6, 9):
        for guess in itertools.product(printable_str, repeat=password_length):
            guess = ''.join(guess)
            guess_hash = crypt.crypt(guess, salt)
            guess_hash = guess_hash[12:]
            if(guess_hash == real_hash):
                print 'password is {} with hash value {}.'.format(guess, guess_hash)
                return
            print 'Guess is {} with hash value {}.'.format(guess, guess_hash)
    return '------------nothing matches-----------------'

print("------------Began------------")
craker()
print("------------End------------")
