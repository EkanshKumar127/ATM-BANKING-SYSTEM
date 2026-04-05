class BankAccount:
    def __init__(self,name,acc_no,pin,balance=0):
        self.name=name
        self.acc_no=acc_no
        self.__pin=pin    #private (encapsulation)
        self.balance=balance
        self.history=[]

    def check_pin(self,pin):
        return pin==self.__pin
    
    def deposit(self,amount):
        if amount<=0:
            print("Ivalid amount!")
        else:
            self.balance+=amount
            self.history.append(f"Deposited {amount}")
            print(f"{amount} credited successfully.")
    
    def withdraw(self,amount ):
        if amount>self.balance:
            print("Insufficient balance!")
        elif amount<=0:
            print("Invalid amount")
        else:
            self.balance-=amount
            self.history.append(f"withdrawn{amount}")
            print(f"{amount} debited successfully.")
    def show_balance(self):
        print("Current balance:",self.balance)

    def show_history(self):
        if not self.history:
            print("No transactions yet")
        else:
            print("\nTransactions history")
            for h in self.history:
                print("-",h)

class Banksystem:
    def __init__(self):
        self.accounts=[]
        
    def createAccount(self):
        name=input("Enter name here:")
        acc_no=float(input("Enter account number:"))
        pin=input("Set Pin:")

        account=BankAccount(name,acc_no,pin)
        self.accounts.append(account)

    def login(self):
        acc_no=float(input("Enter account number:"))
        pin=input("Enter Pin:")
        for acc in self.accounts:
            if acc.acc_no==acc_no and acc.check_pin(pin):
                print(f"Welcome {acc.name}")
                return acc
        print("Invalid Account Number or Pin")
        return None
    #==================main program====================
bank=Banksystem()
while True:
    print("\n============Bank System=============")
    print("1.Create Account")
    print("2.Login")
    print("3.Exit")
    print("5.LogOut")
    
    choice=input( "Enter choice in number:")
    
    if choice=="1":
        bank.createAccount()
    elif choice=="2":
        user=bank.login()

        if user:
            while True:
                print(f"\n==========Welcome{user.name}============")
                print("1.Deposit")
                print("2.Withdraw")
                print("3.Check balance")
                print("4.Transaction History")
                print("5.Logout")

                ch=input("Enter your choice in number:")
                if ch=="1":
                    amt=float(input("Enter amount:"))
                    user.deposit( amt)
                elif ch=="2":
                    amt=float(input("Enter amount:"))
                    user.withdraw(amt)
                elif ch=="3":
                    user.show_balance()
                elif ch=="4":
                    user.show_history()
                elif ch=="5":
                    print("Logout successfully")
                    break
                else:
                    print("Invalid choice!")
    elif choice=="3":
        print("Thank you for using our bank system.")
    else:
        print("Ivalid choice, Try again!")
                   



                