from password_generator import PasswordGenerator
from user import *
from user import User,Credentials



def create_new_user(username,password):
    '''
    Function to create a new user with a username and password
    '''
    new_user = User(user_name,password)
    return new_user

def save_user():
    '''
    Function to save a new user
    '''
    user.save_user(user)
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
    print("Hello, Welcome! \n Choose one of the shortcode to proceed.\n Create New Account-ca \n Login to account-lg")
    short_code=input("").lower().strip()
    if short_code =='ca':
            print('\n')
            print('Create New Account')
            created_user_name =input()
            while True:
                print("\n tp - To type your own pasword,gp - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    print('\n')
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

                    break
                elif password_Choice == 'gp':
                    pwo=PasswordGenerator()
                    pwo.minlen=4
                    pwo.maxlen=6

                    for i in range(1):
                        print(pwo.generate())
                        save_user(created_user_name)
                        print(f"Hello {created_user_name}, Your account has been created succesfully! Your password is: {pwo.generate()}")

        #Need to pick generated password in line 117
        
                else:
                    # print("Invalid password!Try again")
                    save_user(created_user_name,created_user_password)
                    print(f"Hello {created_user_name}, Your account has been created succesfully! Your password is: {password}")
                    # print("_"*15)
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

    while True:
        print("Choose a short code to continue:\n cc - Create a new credential \n dc - Display Credentials \n fc - Find a credential \n gp - Generate A randomn password \n d - Delete credential \n ex - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print('\n')
            print("Account name:")
            account = input().lower()
            print("Your Account username")
            userName = input()
            print("\n")
            while True:
                print(" tp - To type your own pasword if you already have an account, gp, To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    print('\n')
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice == 'gp':
                    pwo=PasswordGenerator()
                    pwo.minlen=4
                    pwo.maxlen=6

                    for i in range(1):
                        print(pwo.generate())
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_new_credential(account,userName,password))
            print('\n')
            print(f"Account Credential for: {account} created successfully. \n UserName: {userName} Password:{password}")
            print('\n')
        elif short_code == "dc":
            if display_accounts_details():
                print("Accounts available: ")
                print('-'* 15)
                for account in display_accounts_details():
                    print(f" Account:{account.account} \n User Name:{userName}\n Password:{password}")
                print('-' * 15)
            else:
                print("You don't have any credentials saved yet..")
        elif short_code == "fc":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 15)
                print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
                print('-' * 15)
            else:
                print("That Credential does not exist")
                print('\n')
        elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*15)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")

        elif short_code == 'gp':
            pwo=PasswordGenerator()
            pwo.minlen=4
            pwo.maxlen=6

            for i in range(1):
                print(pwo.generate())
                print('\n')
            #Need to correct password,to pick generated password.
            print(f" {password} Has been generated succesfull.")
            print('\n')
        elif short_code == 'ex':
            print("Thanks for using password locker...Adios!")
            break
        else:
            print("Wrong entry... Check your entry and try again")
    else:
        print("Please enter a valid input to continue")

if __name__ == '__main__':
    main()

       