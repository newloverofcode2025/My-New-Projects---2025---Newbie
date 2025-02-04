from auth_manager import AuthManager
from budget_manager import BudgetManager

def main():
    # Initialize managers
    auth_manager = AuthManager("budget.db")
    budget_manager = BudgetManager("budget.db")

    print("=== Welcome to the Personal Budgeting App ===")
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            if auth_manager.register(username, password):
                print("Registration successful!")
            else:
                print("Username already exists.")

        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if auth_manager.login(username, password):
                print(f"Welcome, {username}!")
                while True:
                    print("\n=== Budget Menu ===")
                    print("1. Add Income")
                    print("2. Add Expense")
                    print("3. View Summary")
                    print("4. Generate Expense Report")
                    print("5. Logout")
                    budget_choice = input("Enter your choice: ")

                    if budget_choice == "1":
                        amount = float(input("Enter income amount: "))
                        budget_manager.add_income(username, amount)
                        print("Income added successfully!")

                    elif budget_choice == "2":
                        category = input("Enter expense category (e.g., Food, Rent): ")
                        amount = float(input("Enter expense amount: "))
                        budget_manager.add_expense(username, category, amount)
                        print("Expense added successfully!")

                    elif budget_choice == "3":
                        summary = budget_manager.get_summary(username)
                        print("\nSummary:")
                        print(f"Total Income: ${summary['total_income']:.2f}")
                        print(f"Total Expenses: ${summary['total_expenses']:.2f}")
                        print(f"Net Balance: ${summary['net_balance']:.2f}")

                    elif budget_choice == "4":
                        budget_manager.generate_expense_report(username)

                    elif budget_choice == "5":
                        print("Logging out...")
                        break

                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid username or password.")

        elif choice == "3":
            print("Exiting the Budgeting App. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()