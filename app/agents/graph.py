from langgraph.graph import StateGraph, START, END # type: ignore
from langchain_core.messages import BaseMessage, HumanMessage # type: ignore
from state import GroceryState
from prompts import llm, model


def ChatGrocery(state: GroceryState) -> GroceryState:
    prompt = f"""
            "You are a helpful grocery price assistant. "
            "When listing prices, respond in structured JSON matching the GroceryPriceResult schema. "
            "Always include only: product name, app name, numeric price, and product link."
            """
    res = model.invoke(prompt)
    return {"messages": res.content}


graph = StateGraph(GroceryState)
# define nodes

graph.add_node('ChatGrocery', ChatGrocery)
graph.add_edge(START, 'ChatGrocery')
graph.add_edge('ChatGrocery', END)

workflow = graph.compile()

user_input = input()
initial_state = {'messages': [HumanMessage(content=user_input)]}
res = workflow.invoke(initial_state)
print(res)
