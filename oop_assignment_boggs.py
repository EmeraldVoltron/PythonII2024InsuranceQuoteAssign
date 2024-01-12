"""
Abigail Boggs
amboggs@dmacc.edu
Last Edited: 1/11/24
Object Oriented Programming Assignment
"""


class User_Account:
    account_owner = " "

    def __init__(self, account_owner, account_num):
        self.account_owner = account_owner
        self.account_num = account_num
        self.account_balance = 0

    def deposit(self, amount):
        # accepts an amount and adds this amount to the account_balance
        self.account_balance = self.account_balance + amount

    def withdrawal(self, amount):
        # accepts an amount and deducts this amount from the account_balance
        # if the withdrawal amount would cause the amount to go negative,
        if amount > self.account_balance:
            # print that this transaction can't be completed and don't deduct from
            # account_balance
            print("Insufficient Funds, this transaction cannot be completed.")
        else:
            self.account_balance = self.account_balance - amount

    def display(self):
        # should output all information about the user_account
        formatted_price = "$ " + '{:,.2f}'.format(self.account_balance)
        print("Name: " + self.account_owner + "\nAccount Number: " + str(self.account_num) +
              "\nAccount Balance: " + formatted_price)


if __name__ == "__main__":
    account1 = User_Account("Abby", 12345)
    account1.deposit(400)
    account1.withdrawal(250)
    account1.display()

    account2 = User_Account("Bob", 11111)
    account2.deposit(50)
    account2.withdrawal(100)
    account2.display()
