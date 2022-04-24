"""
Class that generates new user instances
"""
user_list = []

def _init_(self,user_name,password):
    self.user_name = user_name
    self.password = password

def save_user(self):
    """
    Method to save new user instance to the user_list
    """
    User.user_list.append(self)
