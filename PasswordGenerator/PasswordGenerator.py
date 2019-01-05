import random
import string
import pyperclip

dict_passwordReqs = {}

def GeneratePassword(dict_passwordReqs = [], numOfPasswords = 1):
    retPasswords = []
    
    UserInput = PullInput(dict_passwordReqs)
    
    for num in list(range(numOfPasswords)):
        retPassword = GenerateRandomString(dict_passwordReqs, UserInput)
        if (num == 0):
            pyperclip.copy(retPassword)
        retPasswords.append(retPassword)

    return retPasswords

def PullInput(dict_passwordReqs = {}):
    retInput = []
    for key, value in dict_passwordReqs.items():
        Input = input(key)
        if(Input == ''):
            retInput.append(0)
        else:
            retInput.append(int(input(key)))
    return retInput

def GenerateRandomString(dict_passwordReqs = {}, UserInput = {}):
    Password = ''
    i = 0
    for key,value in dict_passwordReqs.items():
        for x in list(range(int(UserInput[i]))):
            random.seed()
            Password = Password + ''.join(random.choice(value))
        i += 1
    return PasswordRandomzier(Password)

def PasswordRandomzier(password):   
    return ''.join(random.sample(password,len(password)))

def PasswordGenerator(numOfPasswords = 1):
    dict_passwordReqs['What\'s the minimum length?'] = string.ascii_letters
    dict_passwordReqs['How many special characters?'] = '!@#$%^&*)-'
    dict_passwordReqs['How many numbers?'] = '0123456789'

    print ('Hi there, we will generate a password. Please answer the following')

    print ('Below are three possible passwords. The first password is copied to your clipboard')

    for value in GeneratePassword(dict_passwordReqs):
        print(value)
    return

PasswordGenerator()
    