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
                print('proceed to login')
                print('Username:')
                entered_username =input()
                print('Enter your password')
                entered_password = input()

            while entered_username !=created_user_name or entered_password!=created_user_password:
                print("Invalid username or password")
                print("Username")
                entered_username = input()
                print("Enter your pasword")
                entered_password = input()

            else:
                print(f"{entered_username},welcome to your account")
                print('\n')


        elif short_code =='lg':
            print("Welcome")
            print('Enter username')
            default_user_name =input()

            print('Enter your Password')
            default_user_password =input()
            print('\n')
            while default_user_name != 'testUser' or default_user_password != '09876':
                print("Wrong username or password.username 'testuser' and password '09876'")
                print("Enter user name")
                default_user_name =input()

                print("Enter password")
                default_user_password = input()
                print('\n')

            else:
                print("Login success")
                print('\n')
                print('\n')

        


            











if __name__ == '__main__':
    main()