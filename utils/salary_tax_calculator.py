class SalaryTaxCalculator:
    @staticmethod
    def calculate_salary_tax(annual_salary: float, country: str = "india") -> Dict[str, Any]:
    """
    Calculate tax on salary for India.
    """
    try:
        country = country.lower()
        
        if country == "india":
            # Indian tax slabs for FY 2023-24 (old regime)
            tax = 0
            taxable_income = annual_salary
            
            if taxable_income <= 250000:
                tax = 0
            elif taxable_income <= 500000:
                tax = (taxable_income - 250000) * 0.05
            elif taxable_income <= 1000000:
                tax = 12500 + (taxable_income - 500000) * 0.20
            else:
                tax = 112500 + (taxable_income - 1000000) * 0.30
            
            # Add cess
            cess = tax * 0.04
            total_tax = tax + cess
            
            return {
                "annual_salary": annual_salary,
                "country": "India",
                "taxable_income": taxable_income,
                "income_tax": round(tax, 2),
                "cess": round(cess, 2),
                "total_tax": round(total_tax, 2),
                "net_salary": round(annual_salary - total_tax, 2),
                "effective_tax_rate": round((total_tax / annual_salary) * 100, 2),
                "status": "success"
            }
        else:
            return {"error": "Country must be 'india'", "status": "error"}
    except Exception as e:
        return {"error": str(e), "status": "error"}