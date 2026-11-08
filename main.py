#PROJECT-WealthMatrix
class User:
    def __init__(self, username, initial_balance):
        self.username = username
        self.balance = float(initial_balance)
        self.expenses = []

    def add_income(self, amount):
        amount = float(amount)
        if amount > 0:
            self.balance = self.balance + amount
            print("Amount Successfully added!")
        else:
            print("Invalid amount! Amount must be greater than 0")

    def get_balance(self):
        print(f"Current Balance: {self.balance}")

    def view_profile(self):
        print(f"username: {self.username} | Current balance: {self.balance}")


class Expense:
    def __init__(self, amount, category, description, date):
        self.amount = float(amount)
        self.category = category
        self.description = description
        self.date = date

    def get_expense_details(self):
        print(f"Date: {self.date} | Category: {self.category} | Description: {self.description} | Amount: {self.amount}")


class BudgetManager:
    def __init__(self, user_object):
        self.user = user_object 

    def add_expense(self, amount, category, description, date):
        amount = float(amount)
        if amount > self.user.balance:
            print(f"Insufficient balance! Your current balance is {self.user.balance}")
        else:
            self.user.balance = self.user.balance - amount
            new_expense = Expense(amount, category, description, date)
            self.user.expenses.append(new_expense)
            print("Expense added successfully")

    def view_all_expenses(self):
        print("\n------ ALL EXPENSES --------")
        if len(self.user.expenses) == 0:
            print("No expenses recorded yet")
        else:
            for exp in self.user.expenses:
                exp.get_expense_details()


print("----------- Welcome to Wealthmatrix --------------")
name = input("Enter your name:")
start_balance = input("Enter your initial balance:")

current_user = User(name, start_balance)
manager = BudgetManager(current_user)

while True:
    print("\n------ MENU -------")
    print("1. Add income")
    print("2. Add Expense")
    print("3. Check balance")
    print("4. View expense history")
    print("5. View profile")
    print("6. Exit app")

    choice = input("choose an option (1-6): ")

    if choice == "1":
        inc_amount = input("Enter income amount:")
        current_user.add_income(inc_amount)

    elif choice == "2":
        exp_amount = input("Enter expense amount:")
        cat = input("Enter category (food/travel etc.):")
        desc = input("Enter description:")
        dt = input("Enter date (DD-MM-YYYY): ")
        manager.add_expense(exp_amount, cat, desc, dt)

    elif choice == "3":
        current_user.get_balance()
        
    elif choice == "4":
        manager.view_all_expenses()
        
    elif choice == "5":
        current_user.view_profile()
        
    elif choice == "6":
        print("Thank you for using Wealthmatrix. Goodbye!")
        break
        
    else:
        print("Invalid choice! please select between 1 to 6")

