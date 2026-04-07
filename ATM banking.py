import json

class BankAccount:
    def __init__(self, name, acc_no, pin, balance=0):
        self.name = name
        self.acc_no = acc_no
        self.__pin = pin
        self.balance = balance
        self.history = []

    def check_pin(self, pin):
        return pin == self.__pin

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        else:
            self.balance += amount
            self.history.append(f"Deposited {amount}")
            print(f"{amount} credited successfully")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid amount!")
        else:
            self.balance -= amount
            self.history.append(f"Withdrawn {amount}")
            print(f"{amount} debited successfully")

    def show_balance(self):
        print("Current balance:", self.balance)

    def show_history(self):
        if not self.history:
            print("No transactions yet")
        else:
            print("\nTransaction History:")
            for h in self.history:
                print("-", h)


class BankSystem:
    def __init__(self):
        self.accounts = []
        self.load_data()

    # ---------- SAVE DATA ----------
    def save_data(self):
        data = []
        for acc in self.accounts:
            data.append({
                "name": acc.name,
                "acc_no": acc.acc_no,
                "pin": acc._BankAccount__pin,
                "balance": acc.balance,
                "history": acc.history
            })

        with open("bank_data.json", "w") as f:
            json.dump(data, f, indent=4)

    # ---------- LOAD DATA ----------
    def load_data(self):
        try:
            with open("bank_data.json", "r") as f:
                data = json.load(f)

                for acc in data:
                    account = BankAccount(
                        acc["name"],
                        acc["acc_no"],
                        acc["pin"],
                        acc["balance"]
                    )
                    account.history = acc["history"]
                    self.accounts.append(account)

        except:
            pass

    # ---------- CREATE ACCOUNT ----------
    def createAccount(self):
        name = input("Enter name: ")
        acc_no = input("Enter account number: ")
        pin = input("Set PIN: ")

        account = BankAccount(name, acc_no, pin)
        self.accounts.append(account)
        self.save_data()

        print("Account created successfully!")

    # ---------- LOGIN ----------
    def login(self):
        acc_no = input("Enter account number: ")
        pin = input("Enter PIN: ")

        for acc in self.accounts:
            if acc.acc_no == acc_no and acc.check_pin(pin):
                print(f"Welcome {acc.name}")
                return acc

        print("Invalid login!")
        return None


# ---------- MAIN PROGRAM ----------
bank = BankSystem()

while True:
    print("\n===== ATM SYSTEM =====")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        bank.createAccount()

    elif choice == "2":
        user = bank.login()

        if user:
            while True:
                print("\n1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Transaction History")
                print("5. Logout")

                ch = input("Enter choice: ")

                if ch == "1":
                    amt = int(input("Enter amount: "))
                    user.deposit(amt)
                    bank.save_data()

                elif ch == "2":
                    amt = int(input("Enter amount: "))
                    user.withdraw(amt)
                    bank.save_data()

                elif ch == "3":
                    user.show_balance()

                elif ch == "4":
                    user.show_history()

                elif ch == "5":
                    break

                else:
                    print("Invalid choice!")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")