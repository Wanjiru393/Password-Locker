import random
from user import user_list


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