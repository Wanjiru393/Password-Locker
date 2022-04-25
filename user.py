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


@classmethod
def display_user(cls):
    return cls.user_list

def delete_user(self):
    '''
    delete_account method deletes a  saved account from the list
    '''
    User.user_list.remove(self)
