import os
from utils.mutual_fund_info import MutualFundInfo
from langchain.tools import tool
from typing import List, Dict, Any
from dotenv import load_dotenv

class MutualFundInfoTool:
    def __init__(self):
        load_dotenv()
        self.mutual_fund_service = MutualFundInfo()
        self.mutual_fund_tools_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """
        Setup the tools for mutual fund information retrieval.
        Returns:
            List: A list of tools for mutual fund information retrieval.
        """

        @tool
        def get_mutual_fund_info(scheme_code: str) -> Dict[str, Any]:
            """
            Get mutual fund information using scheme code.
            
            Args:
                scheme_code: Mutual fund scheme code (e.g., '101711')
            
            Returns:
                Dictionary containing mutual fund information
            """
            try:
                data = self.mutual_fund_service.get_fund_info(scheme_code)
                if 'meta' in data:
                    meta = data['meta']
                    latest_nav = data['data'][0] if data['data'] else {}
                    
                    return {
                        "scheme_code": scheme_code,
                        "scheme_name": meta.get('scheme_name', 'N/A'),
                        "fund_house": meta.get('fund_house', 'N/A'),
                        "scheme_type": meta.get('scheme_type', 'N/A'),
                        "scheme_category": meta.get('scheme_category', 'N/A'),
                        "current_nav": latest_nav.get('nav', 0),
                        "nav_date": latest_nav.get('date', 'N/A'),
                        "status": "success"
                    }
                else:
                    return {"error": f"Could not fetch data for scheme code {scheme_code}", "status": "error"}
                    
            except Exception as e:
                return {"error": str(e), "status": "error"}

        return [get_mutual_fund_info]