class User:
    """
    Class that generates new instances of user accounts.
    """
    account_list = [] # Empty account list

    def save_account(self):

        '''
        save_account method saves account objects into account_list
        '''

        User.account_list.append(self)

    def __init__(self,first_name,last_name,phone_number,account_name,email,password):



        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.account_name = account_name
        self.email = email
        self.password = password

    def delete_account(self):

        '''
        delete_account method deletes a saved account from the account_list
        '''

        User.account_list.remove(self)

    @classmethod
    def display_accounts(cls):
        '''
        method that returns the account list
        '''
        return cls.account_list

    def check_existing_account(number):
        '''
        Function that check if a account exists with that number and return a Boolean
        '''
        return User.account_exist(number)
    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns an account that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Account of person that matches the number.
        '''

        for user in cls.account_list:
            if user.phone_number == number:
                return user
