class SalaryCalculator:
    def __init__(self, basic_salary, hra, lta, bonus, other_income):
        # Convert monthly to annual
        self.basic_salary = basic_salary * 12
        self.hra = hra * 12
        self.lta = lta
        self.bonus = bonus
        self.other_income = other_income

    def calculate_gross_salary(self):
        """Calculate gross salary."""
        return self.basic_salary + self.hra + self.lta + self.bonus + self.other_income

    def calculate_taxable_salary(self, deductions_80c):
        """Calculate taxable salary after deductions."""
        gross_salary = self.calculate_gross_salary()
        taxable_salary = gross_salary - deductions_80c
        return max(0, taxable_salary)