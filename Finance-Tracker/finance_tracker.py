import json
import os

class Transaction:
    def __init__(self, transaction_type, description, amount, category):
        self.transaction_type = transaction_type  # "income" or "expense"
        self.description = description
        self.amount = amount
        self.category = category

    def to_dict(self):
        return {
            "type": self.transaction_type,
            "description": self.description,
            "amount": self.amount,
            "category": self.category
        }

class FinanceTracker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.transactions = self.load_transactions()

    def load_transactions(self):
        """Load transactions from the JSON file."""
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        return []

    def save_transactions(self):
        """Save transactions to the JSON file."""
        with open(self.file_path, 'w') as file:
            json.dump(self.transactions, file, indent=4)

    def add_transaction(self, transaction_type, description, amount, category):
        """Add a new transaction."""
        new_transaction = Transaction(transaction_type, description, amount, category)
        self.transactions.append(new_transaction.to_dict())
        self.save_transactions()

    def get_all_transactions(self):
        """Return all transactions."""
        return self.transactions

    def generate_summary(self):
        """Generate a financial summary."""
        total_income = sum(t["amount"] for t in self.transactions if t["type"] == "income")
        total_expenses = sum(t["amount"] for t in self.transactions if t["type"] == "expense")
        net_balance = total_income - total_expenses
        transaction_count = len(self.transactions)
        
        incomes = [t["amount"] for t in self.transactions if t["type"] == "income"]
        expenses = [t["amount"] for t in self.transactions if t["type"] == "expense"]
        
        highest_income = max(incomes) if incomes else 0
        lowest_income = min(incomes) if incomes else 0
        highest_expense = max(expenses) if expenses else 0
        lowest_expense = min(expenses) if expenses else 0

        return {
            "total_income": total_income,
            "total_expenses": total_expenses,
            "net_balance": net_balance,
            "transaction_count": transaction_count,
            "highest_income": highest_income,
            "lowest_income": lowest_income,
            "highest_expense": highest_expense,
            "lowest_expense": lowest_expense
        }