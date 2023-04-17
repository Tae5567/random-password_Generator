
#Random Password Generator

import secrets
import string


#Passwords generated should contain letters, numbers and special characters

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

#set password length
passLength = 12


#generate random password that meets constraints: contains at least 1 number and 1 special character
while True:
    password = '' #initialize empty string
    for i in range(passLength):
        password += ''.join(secrets.choice(alphabet))

    if(any(char in special_chars for char in password) and sum(char in digits for char in password) >= 1):
        break

print("Your password is:", password)
