import requests
from typing import Dict, Any

class RealTimeCryptoPrice:
    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3/simple/price"
        self.params = {}
    def get_crypto_price(self, symbol: str, currency: str = 'usd') -> Dict[str, Any]:
        """Fetch the real-time cryptocurrency price for a given symbol."""
        try:
            self.params = {
                'ids': symbol.lower(),
                'vs_currencies': currency.lower(),
                'include_24hr_change': 'true',
                'include_market_cap': 'true'
            }
            response = requests.get(self.base_url, params=self.params, timeout=10)
            data = response.json()
            return data if response.status_code == 200 else {}
        except Exception as e:
            return {"error": str(e), "status": "error"}