#!/usr/bin/env python3.6
from user import User
def create_account(f_name,l_name,number,account_name,email,password):
    '''
    Function to create a new account
    '''
    new_account = User(f_name,l_name,number,account_name,email,password)
    return new_account

def save_account(self):
    '''
    Function to save account
    '''
    User.save_account(self)

def find_account(number):
    '''
    Function that finds an account by number and returns the account
    '''
    return User.find_by_number(number)

def check_existing_account(number):
    '''
    Function that check if an account exists with that number and return a Boolean
    '''
    return User.display_account()

def display_account():
    '''
    Function that returns all the saved accounts
    '''
    return User.account_list()

def main():
    print("Hello Welcome to your account list. What is your name?")

    user_name = input()


    print(f"Hello {user_name}. what would you like to do?")

    print('\n')


    while True:
                    print("Use these short codes : cc - create a new account, dc - display accounts, fc -find a account, ex -exit the account list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Account")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Phone number ...")
                            number = input()

                            print("account_name")
                            account_name = input()

                            print("Email address ...")
                            email = input()

                            print("password")
                            password = input()


                            save_account(create_account(f_name,l_name,number,account_name,email,password)) # create and save new account.
                            print ('\n')
                            print(f"New Account {f_name} {l_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_account():
                                    print("Here is a list of all your accounts")
                                    print('\n')

                                    for User in account_list():
                                            print(f"{User.f_name} {User.l_name} .....{User.number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any accounts saved yet")
                                    print('\n')
                    elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_account(search_number):
                                    search_account = find_account(search_number)
                                    print(f"{search_account.first_name} {search_account.last_name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_account.phone_number}")
                                    print(f"Email address.......{search_account.email}")
                            else:
                                    print("That account does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':
    main()
