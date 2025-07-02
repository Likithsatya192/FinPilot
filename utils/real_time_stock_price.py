import requests
from typing import Dict, Any

class RealTimeStockPrice:
    def __init__(self):
        self.base_url = "https://query1.finance.yahoo.com/v8/finance/chart"

    def get_stock_price(self, symbol: str) -> Dict[str, Any]:
        """Fetch the real-time stock price for a given symbol."""
        try:
            response = requests.get(url, timeout=10)
            data = response.json()
            return data if response.status_code == 200 else {}
        except Exception as e:
            return {"error": str(e), "status": "error"}
