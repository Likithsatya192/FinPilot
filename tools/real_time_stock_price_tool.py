import os
from utils.real_time_stock_price import get_stock_price
from langchain.tools import tool
from typing import List
from dotenv import load_dotenv
from datetime import datetime
class RealTimeStockPriceTool:
    def __init__(self):
        load_dotenv()
        self.stock_price_service = RealTimeStockPrice()
        self.stock_price_tools_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """
        Setup the tools for real-time stock price retrieval.
        Returns:
            List: A list of tools for real-time stock price retrieval.
        """

        @tool
        def get_stock_price(symbol: str) -> Dict[str, Any]:
            """
            Get real-time stock price for a given symbol.
            
            Args:
                symbol: Stock symbol (e.g., 'AAPL', 'GOOGL', 'TSLA')
            
            Returns:
                Dictionary containing stock price information
            """
            try:
                """Get Current Stock Price for a given symbol."""
                data = stock_price_service.get_stock_price(symbol)
                
                if 'chart' in data and data['chart']['result']:
                    result = data['chart']['result'][0]
                    meta = result['meta']
                    
                    return {
                        "symbol": symbol.upper(),
                        "current_price": meta.get('regularMarketPrice', 0),
                        "previous_close": meta.get('previousClose', 0),
                        "currency": meta.get('currency', 'USD'),
                        "exchange": meta.get('exchangeName', 'Unknown'),
                        "market_state": meta.get('marketState', 'Unknown'),
                        "timestamp": datetime.now().isoformat(),
                        "status": "success"
                    }
                else:
                    return {"error": f"Could not fetch data for {symbol}", "status": "error"}
                    
            except Exception as e:
                return {"error": str(e), "status": "error"}

        return [get_stock_price]
