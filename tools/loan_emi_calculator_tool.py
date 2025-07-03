import os
from utils.loan_emi_calculator import LoanEMICalculator
from langchain.tools import tool
from typing import List, Dict, Any
from dotenv import load_dotenv

class LoanEMICalculatorTool:
    def __init__(self):
        load_dotenv()
        self.loan_emi_calculator_service = LoanEMICalculator()
        self.loan_emi_tools_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """
        Setup the tools for loan EMI calculation.
        Returns:
            List: A list of tools for loan EMI calculation.
        """

        @tool
        def calculate_loan_emi(principal: float, rate: float, tenure_months: int) -> Dict[str, Any]:
            """
            Calculate EMI for a loan.
            
            Args:
                principal: Loan amount
                rate: Annual interest rate (in percentage)
                tenure_months: Loan tenure in months
            
            Returns:
                Dictionary containing EMI calculation details
            """
            try:
                return self.loan_emi_calculator_service.calculate_loan_emi(principal, rate, tenure_months)
            except Exception as e:
                return {"error": str(e), "status": "error"}

        return [calculate_loan_emi]