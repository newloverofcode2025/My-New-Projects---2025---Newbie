from salary_calculator import SalaryCalculator
from tax_calculator import TaxCalculator
from export_to_excel import ExportToExcel

def main():
    print("=== Comprehensive Salary and Tax Calculator ===")
    
    # Input employee details
    name = input("Enter employee name: ")
    basic_salary = float(input("Enter basic salary (annual): "))
    hra = float(input("Enter HRA (annual): "))
    lta = float(input("Enter LTA (annual): "))
    bonus = float(input("Enter bonus (annual): "))
    other_income = float(input("Enter other income (annual): "))
    deductions_80c = float(input("Enter Section 80C deductions (annual): "))
    deductions_medical = float(input("Enter medical insurance premium (Section 80D) (annual): "))
    regime = input("Choose tax regime (old/new/2025): ").lower()

    # Initialize calculators
    salary_calculator = SalaryCalculator(basic_salary, hra, lta, bonus, other_income)
    gross_salary = salary_calculator.calculate_gross_salary()
    taxable_salary = salary_calculator.calculate_taxable_salary(deductions_80c)

    tax_calculator = TaxCalculator(taxable_salary, regime, deductions_medical)
    tax_liability = tax_calculator.calculate_tax()

    # Display results
    print("\n=== Salary and Tax Summary ===")
    print(f"Employee Name: {name}")
    print(f"Gross Salary (Annual): ₹{gross_salary:.2f}")
    print(f"Taxable Salary (Annual): ₹{taxable_salary:.2f}")
    print(f"Tax Liability (Annual): ₹{tax_liability:.2f}")

    # Export to Excel
    export = ExportToExcel(name, gross_salary, taxable_salary, tax_liability)
    export.save_to_excel()

if __name__ == "__main__":
    main()