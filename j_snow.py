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
salt = "$6$aBcDeF$"
real_hash = "qn4wyWpQKwjaKGr02tGUWKcFjl0p90b68.oaaJTFX87UzsSWIzq3ZoAEG0/xUQ1kcYTiHkKqye1Qat6vL4rMZ."

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

    for guess in wordlist:
        guess_hash = crypt.crypt(guess, salt)
        guess_hash = guess_hash[10:]
        if(guess_hash == real_hash):
            print 'password is {} with hash value {}.'.format(guess, guess_hash)
            return
        print 'Wordlist guess is {} with hash value {}.'.format(guess, guess_hash)
    print("------------wordlist runs out-----------------")

    for password_length in range(6, 11):
        for guess in itertools.product(lowercase_str, repeat=password_length):
            guess = ''.join(guess)
            guess_hash = crypt.crypt(guess, salt)
            guess_hash = guess_hash[10:]
            if(guess_hash == real_hash):
                print 'password is {} with hash value {}.'.format(guess, guess_hash)
                return
            print 'Lowercase letter guess is {} with hash value {}.'.format(guess, guess_hash)
    print("------------lowercase runs out-----------------")

    for guess in dictionary:
        guess_hash = crypt.crypt(guess, salt)
        guess_hash = guess_hash[10:]
        if(guess_hash == real_hash):
            print 'password is {} with hash value {}.'.format(guess, guess_hash)
            return
        print 'Dictionary guess is {} with hash value {}.'.format(guess, guess_hash)
    print("------------dictionary runs out-----------------")

    for password_length in range(6, 11):
        for guess in itertools.product(printable_str, repeat=password_length):
            guess = ''.join(guess)
            guess_hash = crypt.crypt(guess, salt)
            guess_hash = guess_hash[10:]
            if(guess_hash == real_hash):
                print 'password is {} with hash value {}.'.format(guess, guess_hash)
                return
            print 'Brute force guess is {} with hash value {}.'.format(guess, guess_hash)
    return '------------nothing matches-----------------'

print("------------Began------------")
craker()
print("------------End------------")
