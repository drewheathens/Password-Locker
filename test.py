import unittest # Importing the unittest module
from account import Account # Importing the contact class

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
        self.new_account = account("James","Muriuki","0712345678","jamesmuriuki","james@ms.com","jimmymuriuki") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.first_name,"James")
        self.assertEqual(self.new_account.last_name,"Muriuki")
        self.assertEqual(self.new_account.phone_number,"0712345678")
        self.assertEqual(self.new_account.account_name,"jamesmuriuki")
        self.assertEqual(self.new_account.email,"james@ms.com")
        self.assertEqual(self.new_account.password, "jimmymuriuki")


if __name__ == '__main__':
    unittest.main()
    def test_save_account(self):
        '''
        test_save_account test case to test if the contact object is saved into the account list
        '''
        self.new_contact.save_contact() #saving the new contact
        self.assertEqual(len(account.account_list), 1)
if __name__== '__main__':
    unittest.main()
    # Items up here...

    def test_save_multiple_account(self):
        '''
        test_save_multiple_accounts to check if we can save multiple acounts
        objects to our account_list
        '''
        self.new_account.save_account()
        test_account = Account("Test","user","0712345678","test@user.com") # new account
        test_account.save_account()
        self.assertEqual(len(Account.account_list),2)

if __name__ == '__main__':
    unittest.main()
