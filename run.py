import random
from user import user_list,Credentials



def create_new_user(username,password):
    '''
    Function to create a new user with a username and password
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()
def display_user():
    """
    Function to display existing user
    """
    return User.display_user()
def login_user(username,password):
    """
    function that checks whether a user exist and then login the user in.
    """
  
    check_user = Credentials.verify_user(username,password)
    return check_user

def create_new_credential(account,userName,password):
    """
    Function that creates new credentials for a given user account
    """
    new_credential = Credentials(account,userName,password)
    return new_credential
def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials. save_details()
def display_accounts_details():
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_credentials()

def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list

    """
    credentials.delete_credentials()

def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_credential(account)
def check_credendtials(account):
    """
    Function that check if a Credentials exists with that account name and return true or false

    """
    return Credentials.if_credential_exist(account)

def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password=Credentials.generatePassword()
    return auto_password
def copy_password(account):
    """
    A funct that copies the password using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    return Credentials.copy_password(account)

def main():

    while True:
        print("Welcome!")
        print('\n')
        print("Select a short code to navigate through:'nu' create new user,'lg' Login to existing account,'ex' exit.")
        short_code = input().lower()
        print('\n')

        if short_code =='nu':
            print('Create your username')
            created_user_name =input()

            print('create password')
            created_user_password =input()

            print('confirm password')
            confirm_password =input()

            while confirm_password !=created_user_password:
                print('Invalid! Password does not match')
                print('Enter your password')
                created_user_password = input()
                print('confirm password')
                confirm_password = input()

            else:
                print(f"{created_user_name}, Account created successfully!")
                print('\n')

        elif short_code =='lg':
            print("Hello!")
            print('Enter username')
            default_user_name =input()

            print('Enter your Password')
            default_user_password =input()
            print('\n')
            while default_user_name !=created_user_name or default_user_password!=created_user_password:
                print("Invalid username or password")
                print("Username")
                default_user_name = input()
                print("Enter your pasword")
                default_user_password = input()

            else:
                print(f"{default_user_name},welcome to your account")
                print('\n')

            

        elif short_code == 'ex':
            break
        else:
            print("Enter valid code to continue")

if __name__ == '__main__':
    main()