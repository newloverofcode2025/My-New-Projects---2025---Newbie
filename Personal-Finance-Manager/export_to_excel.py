import pandas as pd

class ExportToExcel:
    @staticmethod
    def export_transactions(transactions, file_name="transactions.xlsx"):
        """Export transactions to an Excel file."""
        df = pd.DataFrame(transactions, columns=["ID", "Type", "Category", "Amount", "Date"])
        df.to_excel(file_name, index=False)
        print(f"Transactions exported to {file_name}")

    @staticmethod
    def export_goals(goals, file_name="goals.xlsx"):
        """Export financial goals to an Excel file."""
        df = pd.DataFrame(goals, columns=["Name", "Target Amount", "Current Amount"])
        df.to_excel(file_name, index=False)
        print(f"Goals exported to {file_name}")