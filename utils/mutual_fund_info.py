import requests
from typing import Dict, Any

class MutualFundInfo:
    def __init__(self):
        self.base_url = "https://api.mfapi.in/mf"

    def get_fund_info(self, scheme_code: str) -> Dict[str, Any]:
        """Fetch the mutual fund information for a given scheme code."""
        try:
            url = f"{self.base_url}/{scheme_code}"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                try:
                    data = response.json()
                    return data
                except Exception as e:
                    return {"error": f"JSON decode error: {str(e)}. Response text: {response.text}", "status": "error"}
            else:
                return {"error": f"HTTP {response.status_code}: {response.text}", "status": "error"}
        except Exception as e:
            return {"error": str(e), "status": "error"}