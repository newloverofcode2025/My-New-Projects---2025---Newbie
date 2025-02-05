import pandas as pd
import os

class ExportToExcel:
    def __init__(self, name, gross_salary, taxable_salary, tax_liability):
        self.name = name
        self.gross_salary = gross_salary
        self.taxable_salary = taxable_salary
        self.tax_liability = tax_liability

    def save_to_excel(self):
        """Export salary and tax details to an Excel file."""
        data = {
            "Employee Name": [self.name],
            "Gross Salary (Annual)": [self.gross_salary],
            "Taxable Salary (Annual)": [self.taxable_salary],
            "Tax Liability (Annual)": [self.tax_liability]
        }
        df = pd.DataFrame(data)

        # Create output folder if it doesn't exist
        if not os.path.exists("output"):
            os.makedirs("output")

        # Save to Excel with error handling
        try:
            file_path = f"output/{self.name}_salary_tax_details.xlsx"
            df.to_excel(file_path, index=False)
            print(f"Details exported to {file_path}")
        except Exception as e:
            print(f"Failed to export details to Excel: {e}")