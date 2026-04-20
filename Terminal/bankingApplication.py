import random
class InsufficientFund(Exception):
   pass

class Bank:
    user_accounts = {}  # Dictionary to store user details

    def __init__(self, name, dob, fname, acno=None, paswrd="None", bal=0.0):
        self.name = name
        self.date_of_birth = dob
        self.father_name = fname
        self.AccountNo = str(acno) if acno else self.generate_account_number()
        self.password = paswrd
        self.balance = bal
        Bank.user_accounts[self.AccountNo] = self

    def generate_account_number(self):
        return "".join(random.choices("0123456789", k=15))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            if self.balance - amount < 1000:
                print("Minimum Balance is Rs.1000")
                print("Can't withdraw as it exceeds minimum balance")
                print(f"Current Balance: Rs.{self.balance}")
            else:
                self.balance -= amount
                print(f"{amount} withdrawn successfully.")
        else:
            raise InsufficientFund
        except InsufficientFund: 
            print("Insufficient balance or invalid amount.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def display_balance(self):
        print("\nAccount Details:")
        print(f"Account Holder : {self.name}")
        print(f"Account Number : {self.AccountNo}")
        print(f"Current Balance: Rs.{self.balance}")

    def transfer(self, recipient_acno, amount):
        recipient = Bank.user_accounts.get(recipient_acno)
        if recipient and recipient != self:
            #not equal to self ensures that the user is not transfering money to his own account
            if amount > 0 and self.balance - amount >= 1000:
                self.balance -= amount
                recipient.balance += amount
                print(f"Successfully transferred Rs.{amount} to {recipient.name} ({recipient_acno})")
            else:
                print("Transfer failed due to insufficient balance or invalid amount.")
        else:
            print("Recipient account not found or invalid.")

    @staticmethod
    def find_account(acno, paswrd):
        user = Bank.user_accounts.get(str(acno))
        if user and user.password == paswrd:
            return user
        return None

    @staticmethod
    def create_new_account():
        name = input("Enter Full Name: ")
        dob = input("Enter Date of Birth (DD-MM-YYYY): ")
        fname = input("Enter Father's Name: ")
        paswrd = input("Set Your Password: ")
        initial_deposit = float(input("Enter Initial Deposit Amount(Minimum Rs.1000): Rs."))
        while initial_deposit < 1000:
            print("Minimum Balance is Rs.1000. Please try again.")
            initial_deposit = float(input("Enter Initial Deposit Amount(Minimum Rs.1000): Rs."))
        new_user = Bank(name, dob, fname, paswrd=paswrd, bal=initial_deposit)
        print("\nAccount Created Successfully!")
        print(f"Your Account Number: {new_user.AccountNo}")

    @staticmethod
    def remove_account():
        acno = input("Enter your Account Number: ")
        paswrd = input("Enter your Password: ")
        user = Bank.find_account(acno, paswrd)
        if user:
            confirm = input("Are you sure you want to delete your account? (yes/no): ")
            if confirm.lower() == "yes":
                del Bank.user_accounts[acno]
                print("Account successfully deleted.")
            else:
                print("Account deletion canceled.")
        else:
            print("Invalid credentials. Account not found.")

# Preloaded accounts
print("------------ Welcome to LINI Bank! --------------")
holder1 = Bank("Ravi", "10-12-2003", "Gukesh", "112234567891099", "ravi@gukesh12", bal=100000)
holder2 = Bank("Kavi", "11-11-2006", "Mukesh", "123123454567899", "kavi@mukesh34", bal=110000)

while True:
    print("\n------ LINI BANK ------")
    print("1. Create New Account")
    print("2. Login to Existing Account")
    print("3. Remove Account")
    print("4. Exit")
    choice = input("Choose an option (1/2/3/4): ")

    if choice == "1":
        Bank.create_new_account()

    elif choice == "2":
        search_acno = input("Enter Account Number: ")
        search_pass = input("Enter Password: ")

        existing_user = Bank.find_account(search_acno, search_pass)
        if existing_user:
            print(f"\nWelcome {existing_user.name}!")
            while True:
                print("\nBanking Options:")
                print("1. Deposit Money")
                print("2. Withdraw Money")
                print("3. Check Balance")
                print("4. Transfer to Another Account")
                print("5. Log Out")
                action = input("Choose an option (1-5): ")

                if action == "1":
                   try:
                    amount = float(input("Enter deposit amount: Rs."))
                    if amount<0:
                       raise ValueError 
                   except ValueError:
                       print("Amount should not be negative")
                   existing_user.deposit(amount)
		    
                elif action == "2":
                    amount = float(input("Enter withdrawal amount: Rs."))
                    existing_user.withdraw(amount)

                elif action == "3":
                    existing_user.display_balance()

                elif action == "4":
                    to_acno = input("Enter recipient account number: ")
                    amt = float(input("Enter amount to transfer: Rs."))
                    existing_user.transfer(to_acno, amt)

                elif action == "5":
                    confirm = input("Are you sure you want to log out? (yes/no): ")
                    if confirm.lower() == "yes":
                        print("Logged out successfully!")
                        break

                else:
                    print("Invalid choice! Please select 1-5.")
        else:
            print("Invalid account number or password!")

    elif choice == "3":
        Bank.remove_account()

    elif choice == "4":
        print("Thank you for banking with LINI Bank!")
        break

    else:
        print("Invalid Choice! Please select 1-4.")
