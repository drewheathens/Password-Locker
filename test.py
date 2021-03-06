import unittest # Importing the unittest module
from user import User # Importing the user class
import pyperclip

class TestAccount(unittest.TestCase):

    '''
    Test class that defines test cases for the account class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
        # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = User("James","Muriuki","0712345678","jamesmuriuki","james@ms.com","jimmymuriuki") # create account object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.f_name,"James")
        self.assertEqual(self.new_account.l_name,"Muriuki")
        self.assertEqual(self.new_account.number,"0712345678")
        self.assertEqual(self.new_account.account_name,"jamesmuriuki")
        self.assertEqual(self.new_account.email,"james@ms.com")
        self.assertEqual(self.new_account.password, "jimmymuriuki")


    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into the account list
        '''
        self.new_account.save_account() #saving the new account
        self.assertEqual(len(User.account_list), 4)


    def test_save_multiple_account(self):
        '''
        test_save_multiple_accounts to check if we can save multiple accounts
        objects to our account_list
        '''
        self.new_account.save_account()
        test_account = User("Test","user","0712345678","meme","test@user.com","123") # new account
        test_account.save_account()
        self.assertEqual(len(User.account_list),6)

    def test_delete_account(self):
            '''
            test_delete_account to test if we can remove an account from our account list
            '''
            self.new_account.save_account()
            test_account = User("Test","user","0712345678","jimmymuriuki","test@user.com","123") # new account
            test_account.save_account()

            self.new_account.delete_account() # Deleting an account object
            self.assertEqual(len(User.account_list),1)

    def test_find_account_by_number(self):
        '''
        test to check if we can find an account by phone number and display information
        '''

        self.new_account.save_account()
        test_account = User("Test","user","0711223344","jimmymuriuki","test@user.com","123") # new account
        test_account.save_account()

        found_account = User.find_by_number("0711223344")

        self.assertEqual(found_account.email,test_account.email)

    # def test_copy_email(self):
    #     '''
    #     Test to confirm that we are copying the email address from a found account
    #     '''
    #
    #     self.new_account.save_account()
    #     Account.copy_email("0712345678")
    #
    #     self.assertEqual(self.new_account.email,pyperclip.paste())

        @classmethod
        def display_account(cls):
            '''
            method that returns the account list
            '''
            return cls.account_list

if __name__ == '__main__':
    unittest.main()
