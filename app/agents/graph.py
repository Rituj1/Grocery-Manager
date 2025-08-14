from langgraph.graph import StateGraph, START, END
from langchain_core.messages import BaseMessage, HumanMessage
from app.agents import prompts
from state import GroceryState
from prompts import llm, model, GROCERY_PROMPT


def ChatGrocery(state: GroceryState, prompts) -> GroceryState:
    prompt = prompts
    res = llm.invoke(prompt)
    return {"messages": res.content}





graph = StateGraph(GroceryState)
# define nodes

graph.add_node('ChatGrocery', ChatGrocery(prompts))
graph.add_edge(START, 'ChatGrocery')
graph.add_edge('ChatGrocery', END)

workflow = graph.compile()

user_input = input()
initial_state = {'messages': [HumanMessage(content=user_input)]}
res = workflow.invoke(initial_state)
print(res)
