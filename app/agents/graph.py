from langgraph.graph import StateGraph, START, END # type: ignore
from langchain_core.messages import BaseMessage, HumanMessage # type: ignore
from app.agents.state import GroceryState
from app.Utility.Intent import getIntent
from app.providers.Tool import tool
# from app.tools.calling_tool import tool
from app.Utility.Recipe import get_recipe



graph = StateGraph(GroceryState)
# define nodes


graph.add_node('fetchIntent', getIntent.detect_intent_and_ingredients)
graph.add_node('fetchRecipe', get_recipe.step_by_step_recipe)
graph.add_node('searchProductPrize', tool.update_price_comparison)
# graph.add_node('comparePrize', comparePrize)
# graph.add_node('Order', Order)
# graph.add_node('isDeliverd', isDeliverd)


graph.add_edge(START, 'fetchIntent')
graph.add_edge("fetchIntent", 'fetchRecipe')
graph.add_edge('fetchRecipe', 'searchProductPrize')
graph.add_edge('searchProductPrize', END)

workflow = graph.compile()

user_input = input()
initial_state = {'query': user_input}
res = workflow.invoke(initial_state)
print(res)