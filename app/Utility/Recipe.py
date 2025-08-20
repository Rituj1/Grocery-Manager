from app.agents.state import GroceryState, fetch_recipe_model
from langchain_core.messages import SystemMessage, HumanMessage

class getRecipe:
    @staticmethod
    def step_by_step_recipe(state: GroceryState) -> GroceryState:
        # ingredients = state['ingredients']
        dish = state["dish"]

        recipe_prompt = """
        You are a helpful recipe assistant and tell me the recipe for the {dish}
        Note: you have to give me steps into list and list should contain step by step recipe details.
        for example: steps = [step1. .............., step2. ..........., etc]
        """
        query = f"tell me the reipe for {dish}"
        messages = [
            SystemMessage(content=recipe_prompt),
            HumanMessage(content=query)
        ]

        response = fetch_recipe_model.invoke(messages)

        return {
            "steps": response.steps
        }
        
get_recipe = getRecipe()
