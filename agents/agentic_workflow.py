from utils.model_loader import ModelLoader
from prompt_library.system_prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.prebuilt import ToolNode, tools_condition
from tools.currency_converter_tool import CurrencyConverterTool
from tools.loan_emi_calculator_tool import LoanEMICalculatorTool
from tools.mutual_fund_info_tool import MutualFundInfoTool
from tools.real_time_crypto_price_tool import RealTimeCryptoPriceTool
from tools.real_time_stock_price_tool import RealTimeStockPriceTool
from tools.salary_tax_calculator_tool import SalaryTaxCalculatorTool
from tools.sip_calculator_tool import SIPCalculatorTool

class GraphBuilder():
    def __init__(self,model_provider: str = "groq"):
        self.model_loader = ModelLoader(model_provider=model_provider)
        self.llm = self.model_loader.load_llm()
        
        self.tools = []
        
        self.currency_converter_tools = CurrencyConverterTool()
        self.loan_emi_calculator_tools = LoanEMICalculatorTool()
        self.mutual_fund_info_tools = MutualFundInfoTool()
        self.real_time_crypto_price_tools = RealTimeCryptoPriceTool()
        self.real_time_stock_price_tools = RealTimeStockPriceTool()
        self.salary_tax_calculator_tools = SalaryTaxCalculatorTool()
        self.sip_calculator_tools = SIPCalculatorTool()
        
        self.tools.extend([* self.currency_converter_tools.currency_converter_tools_list, 
                           * self.loan_emi_calculator_tools.loan_emi_tools_list,
                           * self.mutual_fund_info_tools.mutual_fund_tools_list,
                           * self.real_time_crypto_price_tools.crypto_price_tools_list,
                           * self.real_time_stock_price_tools.stock_price_tools_list,
                           * self.salary_tax_calculator_tools.tax_calculator_tools_list,
                           * self.sip_calculator_tools.sip_tools_list])

        self.llm_with_tools = self.llm.bind_tools(tools=self.tools)
        
        self.graph = None
        
        self.system_prompt = SYSTEM_PROMPT
    
    
    def agent_function(self,state: MessagesState):
        """Main agent function"""
        user_question = state["messages"]
        input_question = [self.system_prompt] + user_question
        response = self.llm_with_tools.invoke(input_question)
        return {"messages": [response]}
    def build_graph(self):
        graph_builder=StateGraph(MessagesState)
        graph_builder.add_node("agent", self.agent_function)
        graph_builder.add_node("tools", ToolNode(tools=self.tools))
        graph_builder.add_edge(START,"agent")
        graph_builder.add_conditional_edges("agent",tools_condition)
        graph_builder.add_edge("tools","agent")
        graph_builder.add_edge("agent",END)
        self.graph = graph_builder.compile()
        return self.graph
        
    def __call__(self):
        return self.build_graph()