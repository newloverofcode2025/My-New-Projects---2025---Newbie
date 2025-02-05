from database_manager import DatabaseManager
from finance_manager import FinanceManager
from visualization import Visualization
from export_to_excel import ExportToExcel

def main():
    db_manager = DatabaseManager()
    finance_manager = FinanceManager(db_manager)

    while True:
        print("\n=== Personal Finance Manager ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Set Budget")
        print("4. Check Budgets")
        print("5. Add Financial Goal")
        print("6. Update Financial Goal")
        print("7. View Goals")
        print("8. Visualize Spending")
        print("9. Export to Excel")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter income amount: "))
            category = input("Enter income category: ")
            finance_manager.add_income(category, amount)
            print("Income added successfully!")

        elif choice == "2":
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            finance_manager.add_expense(category, amount)
            print("Expense added successfully!")

        elif choice == "3":
            category = input("Enter budget category: ")
            amount = float(input("Enter budget amount: "))
            finance_manager.set_budget(category, amount)
            print("Budget set successfully!")

        elif choice == "4":
            exceeded_budgets = finance_manager.check_budgets()
            if exceeded_budgets:
                print("\nExceeded Budgets:")
                for category, total_spent, limit in exceeded_budgets:
                    print(f"{category}: Spent ${total_spent:.2f}, Limit ${limit:.2f}")
            else:
                print("No budgets exceeded.")

        elif choice == "5":
            name = input("Enter goal name: ")
            target = float(input("Enter target amount: "))
            finance_manager.add_goal(name, target)
            print("Goal added successfully!")

        elif choice == "6":
            name = input("Enter goal name: ")
            amount = float(input("Enter amount to add: "))
            finance_manager.update_goal(name, amount)
            print("Goal updated successfully!")

        elif choice == "7":
            goals = finance_manager.get_goals()
            if goals:
                print("\nFinancial Goals:")
                for name, target, current in goals:
                    print(f"{name}: ${current:.2f} / ${target:.2f}")
            else:
                print("No goals available.")

        elif choice == "8":
            transactions = db_manager.get_transactions()
            Visualization.plot_spending(transactions)

        elif choice == "9":
            transactions = db_manager.get_transactions()
            ExportToExcel.export_transactions(transactions)
            print("Transactions exported to Excel successfully!")

        elif choice == "0":
            db_manager.close()
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()