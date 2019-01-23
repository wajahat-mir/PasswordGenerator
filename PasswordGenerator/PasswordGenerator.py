import random
import string
from Password import *

def NewPasswordGenerator(numOfPasswords = 1):
    
    U1 = UserInput('What\'s the minimum length?', string.ascii_letters)
    U2 = UserInput('How many special characters?', '!@#$%^&*)-')
    U3 = UserInput('How many numbers?', '0123456789')
    User_Input_List = [U1, U2, U3]

    for x in User_Input_List:
        x.poll_user_input()

    for y in range(numOfPasswords):
        password_final = Password()

        for x in User_Input_List:
            x.generate_random_string()
            password_final.generate_simple_password(x)

        print(password_final.generate_random_password())

    return

NewPasswordGenerator()
    