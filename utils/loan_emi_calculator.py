from typing import Dict, Any


class LoanEMICalculator:
    @staticmethod
    def calculate_loan_emi(principal: float, rate: float, tenure_months: int) -> Dict[str, Any]:
        """
        Calculate EMI for a loan.
        """
        try:
            # Convert annual rate to monthly rate
            monthly_rate = rate / (12 * 100)
            
            if monthly_rate == 0:
                # If no interest
                emi = principal / tenure_months
            else:
                # EMI formula: P * r * (1+r)^n / ((1+r)^n - 1)
                emi = principal * monthly_rate * (1 + monthly_rate) ** tenure_months / \
                    ((1 + monthly_rate) ** tenure_months - 1)
            
            total_amount = emi * tenure_months
            total_interest = total_amount - principal
            
            return {
                "principal": round(principal, 2),
                "annual_rate": rate,
                "tenure_months": tenure_months,
                "tenure_years": round(tenure_months / 12, 2),
                "monthly_emi": round(emi, 2),
                "total_amount": round(total_amount, 2),
                "total_interest": round(total_interest, 2),
                "interest_percentage": round((total_interest / principal) * 100, 2),
                "status": "success"
            }
            
        except Exception as e:
            return {"error": str(e), "status": "error"}