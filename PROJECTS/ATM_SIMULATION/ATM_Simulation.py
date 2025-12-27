class ATM:
    def __init__(self):
        self.balance = 10000
        self.card_inserted = False
    
    def insert_card(self):
        self.card_inserted = True
        return "Card inserted"
    
    def check_balance(self):
        if not self.card_inserted:
            return "Insert card first"
        return f"Balance: ₹{self.balance}"
    
    def withdraw(self, amount):
        if not self.card_inserted:
            return "Insert card first"
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrawn ₹{amount}. New balance: ₹{self.balance}"
    
    def deposit(self, amount):
        if not self.card_inserted:
            return "Insert card first"
        self.balance += amount
        return f"Deposited ₹{amount}. New balance: ₹{self.balance}"

# Create ATM
atm = ATM()

# Start ATM service
atm.insert_card()
print("Welcome to Simple ATM!")
print("Commands: 1=Check Balance, 2=Withdraw, 3=Deposit, 0=Exit")

while True:
    cmd = input("\nEnter command (1/2/3/0): ")
    
    if cmd == "0":
        print("Thank you for using Simple ATM!")
        break
    elif cmd == "1":
        print(atm.check_balance())
    elif cmd == "2":
        try:
            money = int(input("Enter amount to withdraw: "))
            print(atm.withdraw(money))
        except:
            print("Enter valid number")
    elif cmd == "3":
        try:
            money = int(input("Enter amount to deposit: "))
            print(atm.deposit(money))
        except:
            print("Enter valid number")
    else:
        print("Invalid command. Use: 1, 2, 3, or 0")