#!/usr/bin/env python3.6
from user import User
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
                            p_number = input()

                            print("Email address ...")
                            e_address = input()


                            save_accounts(create_account(f_name,l_name,p_number,e_address)) # create and save new account.
                            print ('\n')
                            print(f"New Account {f_name} {l_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_accounts():
                                    print("Here is a list of all your contacts")
                                    print('\n')

                                    for account in display_accounts():
                                            print(f"{user.first_name} {user.last_name} .....{user.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any accounts saved yet")
                                    print('\n')

                    elif short_code == 'fc':

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
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':

    main()
