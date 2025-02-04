from finance_tracker import FinanceTracker

def initialize_transactions():
    """Initialize the transactions.json file if it doesn't exist."""
    import os
    import json
    if not os.path.exists('transactions.json'):
        with open('transactions.json', 'w') as file:
            json.dump([], file)

def main():
    # Initialize the transactions.json file
    initialize_transactions()

    # Initialize the FinanceTracker
    finance_tracker = FinanceTracker("transactions.json")

    while True:
        print("\n=== Personal Finance Tracker ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View All Transactions")
        print("4. Generate Financial Summary")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter income description: ")
            amount = float(input("Enter income amount: "))
            category = input("Enter income category (e.g., Salary, Gift): ")
            finance_tracker.add_transaction("income", description, amount, category)
            print("Income added successfully!")

        elif choice == "2":
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category (e.g., Food, Rent): ")
            finance_tracker.add_transaction("expense", description, amount, category)
            print("Expense added successfully!")

        elif choice == "3":
            transactions = finance_tracker.get_all_transactions()
            if transactions:
                print("\nAll Transactions:")
                for t in transactions:
                    print(f"Type: {t['type']}, Description: {t['description']}, Amount: {t['amount']}, Category: {t['category']}")
            else:
                print("No transactions available.")

        elif choice == "4":
            summary = finance_tracker.generate_summary()
            print("\nFinancial Summary:")
            print(f"Total Income: ${summary['total_income']:.2f}")
            print(f"Total Expenses: ${summary['total_expenses']:.2f}")
            print(f"Net Balance: ${summary['net_balance']:.2f}")
            print(f"Number of Transactions: {summary['transaction_count']}")
            print(f"Highest Income: ${summary['highest_income']:.2f}")
            print(f"Lowest Income: ${summary['lowest_income']:.2f}")
            print(f"Highest Expense: ${summary['highest_expense']:.2f}")
            print(f"Lowest Expense: ${summary['lowest_expense']:.2f}")

        elif choice == "5":
            print("Exiting the Finance Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()