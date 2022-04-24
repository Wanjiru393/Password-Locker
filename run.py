import random
from user import User


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
                print('proceed to login')
                print('Username:')
                entered_username =input()
                print('Enter your password')
                entered_password = input()











if __name__ == '__main__':
    main()