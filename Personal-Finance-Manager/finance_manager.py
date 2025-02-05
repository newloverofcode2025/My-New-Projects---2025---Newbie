from datetime import datetime

class FinanceManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def add_income(self, category, amount):
        """Add income to the database."""
        date = datetime.now().strftime("%Y-%m-%d")
        self.db_manager.add_transaction("income", category, amount, date)

    def add_expense(self, category, amount):
        """Add an expense to the database."""
        date = datetime.now().strftime("%Y-%m-%d")
        self.db_manager.add_transaction("expense", category, amount, date)

    def set_budget(self, category, limit_amount):
        """Set a budget for a category."""
        self.db_manager.set_budget(category, limit_amount)

    def get_budgets(self):
        """Retrieve all budgets."""
        return self.db_manager.get_budgets()

    def check_budgets(self):
        """Check if any budgets have been exceeded."""
        budgets = self.db_manager.get_budgets()
        transactions = self.db_manager.get_transactions()

        category_totals = {}
        for _, transaction_type, category, amount, _ in transactions:
            if transaction_type == "expense":
                category_totals[category] = category_totals.get(category, 0) + amount

        exceeded_budgets = []
        for category, limit in budgets.items():
            total_spent = category_totals.get(category, 0)
            if total_spent > limit:
                exceeded_budgets.append((category, total_spent, limit))

        return exceeded_budgets

    def add_goal(self, name, target_amount):
        """Add a financial goal."""
        self.db_manager.add_goal(name, target_amount)

    def get_goals(self):
        """Retrieve all financial goals."""
        return self.db_manager.get_goals()

    def update_goal(self, name, amount):
        """Update the current amount of a financial goal."""
        self.db_manager.update_goal(name, amount)