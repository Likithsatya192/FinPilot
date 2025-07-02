import requests
from typing import Dict, Any

class RealTimeStockPrice:
    def __init__(self):
        self.base_url = "https://query1.finance.yahoo.com/v8/finance/chart"
        self.params = {}

    def get_stock_price(self, symbol: str) -> Dict[str, Any]:
        """Fetch the real-time stock price for a given symbol."""
        try:
            url = f"{self.base_url}/{symbol}"
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

    def get_stock_summary(self, symbol: str) -> Dict[str, Any]:
        """Fetch the stock summary for a given symbol."""
        try:
            url = f"{self.base_url}/{symbol}"
            self.params = {
                'modules': 'summaryDetail,defaultKeyStatistics,assetProfile'
            }
            response = requests.get(url, params=self.params, timeout=10)
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
