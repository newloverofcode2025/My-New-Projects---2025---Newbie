import sqlite3
import matplotlib.pyplot as plt

class BudgetManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Create the transactions table if it doesn't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                type TEXT NOT NULL,
                category TEXT,
                amount REAL NOT NULL
            )
        """)
        self.conn.commit()

    def add_income(self, username, amount):
        """Add income for a user."""
        self.cursor.execute("INSERT INTO transactions (username, type, amount) VALUES (?, 'income', ?)", (username, amount))
        self.conn.commit()

    def add_expense(self, username, category, amount):
        """Add an expense for a user."""
        self.cursor.execute("INSERT INTO transactions (username, type, category, amount) VALUES (?, 'expense', ?, ?)", (username, category, amount))
        self.conn.commit()

    def get_summary(self, username):
        """Get the total income, total expenses, and net balance for a user."""
        self.cursor.execute("SELECT SUM(amount) FROM transactions WHERE username = ? AND type = 'income'", (username,))
        total_income = self.cursor.fetchone()[0] or 0

        self.cursor.execute("SELECT SUM(amount) FROM transactions WHERE username = ? AND type = 'expense'", (username,))
        total_expenses = self.cursor.fetchone()[0] or 0

        net_balance = total_income - total_expenses
        return {
            "total_income": total_income,
            "total_expenses": total_expenses,
            "net_balance": net_balance
        }

    def generate_expense_report(self, username):
        """Generate a pie chart and bar graph for expense categorization."""
        self.cursor.execute("SELECT category, SUM(amount) FROM transactions WHERE username = ? AND type = 'expense' GROUP BY category", (username,))
        data = self.cursor.fetchall()

        if not data:
            print("No expenses to report.")
            return

        categories, amounts = zip(*data)

        # Pie Chart
        plt.figure(figsize=(10, 5))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%')
        plt.title("Expense Distribution")
        plt.show()

        # Bar Graph
        plt.figure(figsize=(10, 5))
        plt.bar(categories, amounts, color='skyblue')
        plt.title("Expense Breakdown")
        plt.xlabel("Category")
        plt.ylabel("Amount ($)")
        plt.show()