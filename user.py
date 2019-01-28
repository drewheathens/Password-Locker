class user:
    """
    Class that generates new instances of user accounts.
    """
    account_list = [] # Empty account list
      # Init method up here
    def save_account(self):

        '''
        save_account method saves account objects into account_list
        '''

        Account.account_list.append(self)

    def __init__(self,first_name,last_name,phone_number,account_name,email,password):

      # docstring removed for simplicity

        

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

        Contact.account_list.remove(self)

    @classmethod
    def display_contacts(cls):
        '''
        method that returns the contact list
        '''
        return cls.contact_list
