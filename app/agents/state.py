from typing import TypedDict, List
from langchain_core.messages import AnyMessage

class GroceryState(TypedDict):
    messages: List[AnyMessage]