class Bank:
    Bank_Name = "SBI"
    Branch_Name = "Gajhodhar Branch, FurfuriNagar"


class Account:
    def __init__(self):
        self.Account_Number = 0
        self.Name = ""
        self.balance = 0

    def Create_Account(self):
        self.Account_Number = int(input("Enter Account Number"))
        self.Name = input("Enter Your Name ")
        print("Account Created Successfully ")

    def Account_Info(self):
        print("\n----- Account Information -----")
        print("Bank Name:", Bank.Bank_Name)
        print("Branch Name:", Bank.Branch_Name)
        print("Account Number:", self.Account_Number)
        print("Name:", self.Name)


class Transaction:

    def __init__(self, account):
        self.account = account

    def Deposit(self, Deposit_Amount):
        self.account.balance = self.account.balance + Deposit_Amount
        print("Money Deposited")

    def Withdraw(self, amount):
        if self.account.balance >= amount:
            self.account.balance -= amount
            print(amount, "Withdrawn")
        else:
            print("Insufficient Balance")

    def Check_Balance(self):
        print("Your Account Balance is:", self.account.balance)

    def Send_Money(self, sending_amount):
        if self.account.balance >= sending_amount:
            self.account.balance -= sending_amount
            print("Money Transferred")
        else:
            print("Insufficient Balance")


acc = Account()
trans = Transaction(acc)



while (True):
    choice = int(input(
        "Select the Operation\n"
        "1. Create Account\n"
        "2. Deposit Money\n"
        "3. Withdraw Money\n"
        "4. Check Balance\n"
        "5. Transfer Money\n"
        "6. Account Information\n"
        "Enter your choice: "
    ))

    match choice:
        case 1:
            acc.Create_Account()

        case 2:
            amount = int(input("Enter Deposit Amount: "))
            trans.Deposit(amount)

        case 3:
            amount = int(input("Enter Withdrawal Amount: "))
            trans.Withdraw(amount)

        case 4:
            trans.Check_Balance()

        case 5:
            amount = int(input("Enter Transfer Amount: "))
            trans.Send_Money(amount)

        case 6:
            acc.Account_Info()

        case _:
            print("Invalid Choice")