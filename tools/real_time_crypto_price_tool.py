import os
from dotenv import load_dotenv
from utils.real_time_crypto_price import RealTimeCryptoPrice
from langchain.tools import tool
from typing import List, Dict, Any
from datetime import datetime

class RealTimeCryptoPriceTool:
    def __init__(self):
        load_dotenv()
        self.crypto_price_service = RealTimeCryptoPrice()
        self.crypto_price_tools_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """
        Setup the tools for real-time cryptocurrency price retrieval.
        Returns:
            List: A list of tools for real-time cryptocurrency price retrieval.
        """

        @tool
        def get_crypto_price(symbol: str, currency: str = 'usd') -> Dict[str, Any]:
            """
            Get real-time cryptocurrency price.
            
            Args:
                symbol: Crypto symbol (e.g., 'bitcoin', 'ethereum', 'cardano')
            
            Returns:
                Dictionary containing crypto price information
            """
            try:
                data = self.crypto_price_service.get_crypto_price(symbol, currency)
                if symbol.lower() in data:
                    crypto_data = data[symbol.lower()]
            
                    return {
                        "symbol": symbol.lower(),
                        "price_usd": crypto_data.get('usd', 0),
                        "price_inr": crypto_data.get('inr', 0),
                        "24h_change": crypto_data.get('usd_24h_change', 0),
                        "market_cap_usd": crypto_data.get('usd_market_cap', 0),
                        "timestamp": datetime.now().isoformat(),
                        "status": "success"
                    }
                else:
                    return {"error": f"Could not fetch data for {symbol}", "status": "error"}
                    
            except Exception as e:
                return {"error": str(e), "status": "error"}

        return [get_crypto_price]