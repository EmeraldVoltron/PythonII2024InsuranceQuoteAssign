"""
Abigail Boggs
amboggs@dmacc.edu
Last Edited: 1/12/2024
Unit testing for Object-Oriented Programming Assignment
"""
import unittest
from oop_assignment_boggs import User_Account


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.account = User_Account("Abby", 12345)

    def tearDown(self):
        del self.account

    def test_account_attributes(self):
        # tests if the values are initialized correctly
        self.assertEqual(self.account.account_owner, "Abby")
        self.assertEqual(self.account.account_num, 12345)
        # balance starts out as 0
        self.assertEqual(self.account.account_balance, 0)

    def test_deposit_method(self):
        # tests if balance is the right amount after deposit, 200
        self.account.deposit(200)
        self.assertEqual(self.account.account_balance, 200)

    def test_withdrawal_method_normal(self):
        # tests if the balance is the right amount after withdrawal
        self.account.deposit(200) # deposit money first
        self.account.withdrawal(50)
        self.assertEqual(self.account.account_balance, 150)

    def test_withdrawal_method_insufficient_funds(self):
        self.account.deposit(50)
        self.account.withdrawal(100)
        # tests to see if the balance remains the same, because it
        # can't withdraw with insufficient funds
        self.assertEqual(self.account.account_balance, 50)

    def test_display_method(self):
        comparison = "Name: Abby\nAccount Number: 12345\nAccount Balance: $ 0.00"
        self.assertEqual(self.account.display(), comparison)


if __name__ == "__main__":
    unittest.main()

