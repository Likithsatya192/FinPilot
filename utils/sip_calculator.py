from typing import Dict, Any

class SIPCalculator:
    @staticmethod
    def calculate_sip(monthly_investment: float, annual_return: float, tenure_years: int) -> Dict[str, Any]:
        """
        Calculate SIP (Systematic Investment Plan) returns.
        """
        try:
            # Convert annual return to monthly return
            monthly_return = annual_return / (12 * 100)
            total_months = tenure_years * 12
            
            if monthly_return == 0:
                # If no return
                maturity_amount = monthly_investment * total_months
            else:
                # SIP formula: M * [((1+r)^n - 1) / r] * (1+r)
                maturity_amount = monthly_investment * \
                                (((1 + monthly_return) ** total_months - 1) / monthly_return) * \
                                (1 + monthly_return)
            
            total_invested = monthly_investment * total_months
            total_returns = maturity_amount - total_invested
            
            return {
                "monthly_investment": round(monthly_investment, 2),
                "annual_return": annual_return,
                "tenure_years": tenure_years,
                "total_months": total_months,
                "total_invested": round(total_invested, 2),
                "maturity_amount": round(maturity_amount, 2),
                "total_returns": round(total_returns, 2),
                "returns_percentage": round((total_returns / total_invested) * 100, 2),
                "status": "success"
            }
            
        except Exception as e:
            return {"error": str(e), "status": "error"}