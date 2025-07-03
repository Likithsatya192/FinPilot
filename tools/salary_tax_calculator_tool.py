import os
from utils.salary_tax_calculator import SalaryTaxCalculator
from langchain.tools import tool
from typing import List, Dict, Any
from dotenv import load_dotenv

class SalaryTaxCalculatorTool:
    def __init__(self):
        load_dotenv()
        self.tax_calculator_service = SalaryTaxCalculator()
        self.tax_calculator_tools_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """
        Setup the tools for salary tax calculation.
        Returns:
            List: A list of tools for salary tax calculation.
        """

        @tool
        def calculate_salary_tax(annual_salary: float, country: str = "india") -> Dict[str, Any]:
            """
            Calculate tax on salary for India or US.
            
            Args:
                annual_salary: Annual salary amount
                country: Country for tax calculation ('india')
            
            Returns:
                Dictionary containing tax calculation details
            """
            try:
                return self.tax_calculator_service.calculate_salary_tax(annual_salary, country)
            except Exception as e:
                return {"error": str(e), "status": "error"}

        return [calculate_salary_tax]