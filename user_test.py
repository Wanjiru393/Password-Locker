import unittest
from user import Credentials
from user import user_list


class TestClass(unittest.TestCase):
    """
    A test class that defines cases for the User Class.
    """
    def setUp(self):
        '''
        Method that runs before each individual test methods
        '''
        self.new_user= User('Wanjiru','rg44e')
    
    def test_init(self):
        """
        test case to chek if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.user_name, 'Wanjiru')
        self.assertEqual(new_user.password, 'rg44e')
    
    def test_save_user(self):
        """
        test case to test if a new user instance has been saved into the User list

        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)