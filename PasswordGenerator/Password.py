import random

class UserInput:

    def __init__(self, userQuery, queryOption):
        self.UserQuery = userQuery
        self.QueryOption = queryOption  
        self.Input = 0
        self.random_sample = ""

    def poll_user_input(self):
        self.Input = int(input(self.UserQuery))

    def generate_random_string(self):
        self.random_sample = ""
        for x in list(range(int(self.Input))):
            random.seed()
            self.random_sample = self.random_sample + ''.join(random.choice(self.QueryOption))
        return

class Password:

    def __init__(self):
        self.FinalPassword = ""

    def generate_simple_password(self, User_Input):
        self.FinalPassword = self.FinalPassword + ''.join(User_Input.random_sample)

    def generate_random_password(self):
        random.seed()
        return ''.join(random.sample(self.FinalPassword,len(self.FinalPassword)))