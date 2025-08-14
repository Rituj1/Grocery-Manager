from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from pydantic import BaseModel, HttpUrl
from dotenv import load_dotenv
load_dotenv()

class GroceryPriceResult(BaseModel):
    product_name: str
    app_name: str 
    price: float
    link: HttpUrl


grocery_system_prompt = (
    "You are a helpful grocery price assistant. "
    "Given a user request for grocery items, decide whether to use the price comparison tool. "
    "When listing prices, respond in structured JSON matching the GroceryPriceResult schema. "
    "Always include: product name, app name, numeric price, and product link."
)


GROCERY_PROMPT = ChatPromptTemplate.from_messages([
    ("system", grocery_system_prompt),
    ("human", "{user_input}")
])

model = ChatGroq(temperature=0, model_name="llama3-70b-8192")
llm = model.with_structured_output(GroceryPriceResult)