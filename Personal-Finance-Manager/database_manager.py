import sqlite3

class DatabaseManager:
    def __init__(self, db_path="finance.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Create the necessary tables if they don't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                date TEXT NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS budgets (
                category TEXT PRIMARY KEY,
                limit_amount REAL NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS goals (
                name TEXT PRIMARY KEY,
                target_amount REAL NOT NULL,
                current_amount REAL DEFAULT 0
            )
        """)
        self.conn.commit()

    def add_transaction(self, transaction_type, category, amount, date):
        """Add a transaction to the database."""
        self.cursor.execute("""
            INSERT INTO transactions (type, category, amount, date)
            VALUES (?, ?, ?, ?)
        """, (transaction_type, category, amount, date))
        self.conn.commit()

    def set_budget(self, category, limit_amount):
        """Set a budget for a category."""
        self.cursor.execute("""
            INSERT OR REPLACE INTO budgets (category, limit_amount)
            VALUES (?, ?)
        """, (category, limit_amount))
        self.conn.commit()

    def get_budgets(self):
        """Retrieve all budgets."""
        self.cursor.execute("SELECT category, limit_amount FROM budgets")
        return dict(self.cursor.fetchall())

    def get_transactions(self):
        """Retrieve all transactions."""
        self.cursor.execute("SELECT * FROM transactions")
        return self.cursor.fetchall()

    def add_goal(self, name, target_amount):
        """Add a financial goal."""
        self.cursor.execute("""
            INSERT INTO goals (name, target_amount)
            VALUES (?, ?)
        """, (name, target_amount))
        self.conn.commit()

    def get_goals(self):
        """Retrieve all financial goals."""
        self.cursor.execute("SELECT name, target_amount, current_amount FROM goals")
        return self.cursor.fetchall()

    def update_goal(self, name, amount):
        """Update the current amount of a financial goal."""
        self.cursor.execute("""
            UPDATE goals
            SET current_amount = current_amount + ?
            WHERE name = ?
        """, (amount, name))
        self.conn.commit()

    def close(self):
        """Close the database connection."""
        self.conn.close()