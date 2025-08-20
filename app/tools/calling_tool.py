from app.providers.Tool import Tool
from app.agents.state import GroceryState

class CallingTool:
    @staticmethod
    def fetch_recipe(state: GroceryState) -> GroceryState:
        return Tool.search(state)
    
tool = CallingTool()