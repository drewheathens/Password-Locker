import unittest # Importing the unittest module
from user import user # Importing the user class

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
        self.new_account = user("James","Muriuki","0712345678","jamesmuriuki","james@ms.com","jimmymuriuki") # create contact object


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
        self.assertEqual(len(Account.account_list), 1)
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
    # More tests above
    def test_delete_account(self):
            '''
            test_delete_account to test if we can remove an account from our account list
            '''
            self.new_account.save_account()
            test_account = Account("Test","user","0712345678","test@user.com") # new account
            test_account.save_account()

            self.new_account.delete_account()# Deleting an account object
            self.assertEqual(len(Account.account_list),1)
if __name__ == '__main__':
    unittest.main()
    def test_find_account_by_number(self):
        '''
        test to check if we can find an account by phone number and display information
        '''

        self.new_account.save_account()
        test_account = Account("Test","user","0711223344","test@user.com") # new account
        test_account.save_account()

        found_account = account.find_by_number("0711223344")

        self.assertEqual(found_account.email,test_account.email)
