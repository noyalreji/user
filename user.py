class User:		
    def __init__(self, name, email_id):
        self.name = name
        self.email = email_id
        self.account_balance = 0
        # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self
    # add a withdrawal method
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    # BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
    def transfer_money(self, user, amount):
        self.account_balance -= amount
        user.account_balance += amount
        return self
    
    # display user balance
    def display_user_balance(self):
        print(f'User: {self.name} Balance: {self.account_balance}')
        return self
#Create 3 instances for the User class
user1 = User('Noyal Jacob', 'noyal@gmail.com')
user2 = User('Mike Jon', 'mja@gmail.com')
user3 = User('Dwayne Johnson', 'rock@cooking.com')

print(user1.name, user1.email, user1.account_balance)
print(user2.name, user2.email, user2.account_balance)
print(user3.name, user3.email, user3.account_balance)

# Have the first user make 3 deposits and 1 withdrawal and then display their balance
user1.make_deposit (1300)
user1.make_deposit (1200)
user1.make_deposit (1300)
user1.make_withdrawal (2200)

user1.display_user_balance()

# Have the first user make 3 deposits and 1 withdrawal and then display their balance
user2.make_deposit (1300)
user2.make_deposit (1200)
user2.make_withdrawal (200)
user2.make_withdrawal (200)

user2.display_user_balance()

# Have the third user make 1 deposits and 3 withdrawals and then display their balance
user3.make_deposit (6200)
user3.make_withdrawal (1200)
user3.make_withdrawal (1200)
user3.make_withdrawal (1200)

user3.display_user_balance()

# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances

user1.transfer_money(user2,200)

user1.display_user_balance()
user2.display_user_balance()