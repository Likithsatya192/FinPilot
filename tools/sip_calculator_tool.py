import os
from utils.sip_calculator import SIPCalculator
from langchain.tools import tool
from typing import List, Dict, Any
from dotenv import load_dotenv

class SIPCalculatorTool:
    def __init__(self):
        load_dotenv()
        self.sip_calculator_service = SIPCalculator()
        self.sip_tools_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """
        Setup the tools for SIP calculation.
        Returns:
            List: A list of tools for SIP calculation.
        """

        @tool
        def calculate_sip_amount(principal: float, rate: float, tenure_months: int) -> Dict[str, Any]:
            """
            Calculate SIP amount for a given principal, rate, and tenure.
            
            Args:
                principal: Monthly investment amount
                rate: Expected annual return rate (in percentage)
                tenure_months: Investment tenure in months
            
            Returns:
                Dictionary containing SIP calculation details
            """
            try:
                return self.sip_calculator_service.calculate_sip_amount(principal, rate, tenure_months)
            except Exception as e:
                return {"error": str(e), "status": "error"}

        return [calculate_sip_amount]