from app.agents.state import GroceryState, intent_model
from app.agents.prompts import intent_prompt
from langchain_core.messages import SystemMessage, HumanMessage


class Intent:
    def detect_intent_and_ingredients(self, state: GroceryState) -> GroceryState:
        query = state['query']
        message = [
            SystemMessage(content=intent_prompt),
            HumanMessage(content=query)
        ]
        res = intent_model.invoke(message)
        return {"intent": res.intent, "ingredients": res.ingredients, "dish": res.dish}

getIntent = Intent()

