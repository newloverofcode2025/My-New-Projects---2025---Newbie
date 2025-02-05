class TaxCalculator:
    def __init__(self, taxable_salary, regime, medical_deduction):
        self.taxable_salary = taxable_salary
        self.regime = regime
        self.medical_deduction = medical_deduction

    def calculate_tax(self):
        """Calculate tax based on the chosen regime."""
        if self.regime == "old":
            return self._calculate_old_regime_tax()
        elif self.regime == "new":
            return self._calculate_new_regime_tax_2023()
        elif self.regime == "2025":
            return self._calculate_new_regime_tax_2025()
        else:
            raise ValueError("Invalid tax regime selected.")

    def _calculate_old_regime_tax(self):
        """Calculate tax under the old regime."""
        taxable = self.taxable_salary
        if taxable <= 250000:
            return 0
        elif taxable <= 500000:
            return (taxable - 250000) * 0.05
        elif taxable <= 1000000:
            return 12500 + (taxable - 500000) * 0.2
        else:
            return 112500 + (taxable - 1000000) * 0.3

    def _calculate_new_regime_tax_2023(self):
        """Calculate tax under the new regime (2023)."""
        taxable = self.taxable_salary
        if taxable <= 300000:
            return 0
        elif taxable <= 600000:
            return (taxable - 300000) * 0.05
        elif taxable <= 900000:
            return 15000 + (taxable - 600000) * 0.1
        elif taxable <= 1200000:
            return 45000 + (taxable - 900000) * 0.15
        elif taxable <= 1500000:
            return 90000 + (taxable - 1200000) * 0.2
        else:
            return 150000 + (taxable - 1500000) * 0.3

    def _calculate_new_regime_tax_2025(self):
        """Calculate tax under the new regime (2025)."""
        # Placeholder for future updates
        return self._calculate_new_regime_tax_2023()