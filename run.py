#!/usr/bin/env python3.6
from user import user

def create_account(fname,lname,phone,email):
    '''
    Function to create a new account
    '''
    new_contact = Account(fname,lname,phone,aname,email,password)
    return new_account

def save_accounts(account):
    '''
    Function to save account
    '''
    contact.save_account()

def del_account(account):
    '''
    Function to delete an account
    '''
    contact.delete_account()

def find_account(number):
    '''
    Function that finds a account by number and returns the account
    '''
    return Account.find_by_number(number)

def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Account.display_accounts()

def main():
    print("Hello Welcome to your account list. What is your name?")

    account_name = input()

    print(f"Hello {account_name}. what would you like to do?")
    print('\n')

    while True:
    print("Use these short codes : 1 - create a new account, 2 - display accounts, 3 -find an account, ex - exit the account list ")

    short_code = input().lower()

    if short_code == '1':
        
                            print("New Account")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Phone number ...")
                            p_number = input()


                            print("Email address ...")
                            e_address = input()

                            print("password ...")
                            password = input()


                            save_Accounts(create_account(f_name,l_name,p_number,e_address,password)) # create and save new account.
                            print ('\n')
                            print(f"New Account {f_name} {l_name} created")
                            print ('\n')

                    elif short_code == '2':

                            if display_accounts():
                                    print("Here is a list of all your accountts")
                                    print('\n')

                                    for account in display_accounts():
                                            print(f"{account.first_name} {account.last_name} .....{account.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any acounts saved yet")
                                    print('\n')

                    elif short_code == '3':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_accounts(search_number):
                                    search_account = find_account(search_number)
                                    print(f"{search_account.first_name} {search_account.last_name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_account.phone_number}")
                                    print(f"Email address.......{search_account.email}")
                            else:
                                    print("That account does not exist")

                    elif short_code == "ex":
                            print("Ciao .......")
                            break
                    else:
                            print("I really didn't get that. Please use 1, 2, 3 or ex")


if __name__ == '__main__':

    main()
