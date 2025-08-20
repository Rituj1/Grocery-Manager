from typing import TypedDict, List, Dict, Any, Annotated
from pydantic import BaseModel, HttpUrl
from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()

class GroceryPriceResult(BaseModel):
    product_name: str
    app_name: str 
    price: float
    link: HttpUrl


class FetchRecipe(BaseModel):
    steps: List[str]


class GroceryState(TypedDict):
    query: str
    messages: List[Dict[str, Any]]   
    intent: List[str]                      
    ingredients: List[str]  
    dish: str
    steps: List[str]    
    price_comparison: Dict[str, Dict[str, List[GroceryPriceResult]]]
    chosen_app: str                  
    order_status: str  

              
class IntentResult(BaseModel):
    intent: List[str]               
    ingredients: List[str]   
    dish: List[str] 


class PriceComparisonResult(BaseModel):
    ingredient: str
    prices: List[GroceryPriceResult]





model = ChatGroq(temperature=0, model_name="llama3-70b-8192")


grocery_prize = model.with_structured_output(GroceryPriceResult)
intent_model = model.with_structured_output(IntentResult)
price_comparison_model = model.with_structured_output(PriceComparisonResult)
fetch_recipe_model = model.with_structured_output(FetchRecipe)