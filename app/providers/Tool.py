import os
from typing import List, Dict
from langchain_community.tools.tavily_search import TavilySearchResults
import requests
from app.agents.state import GroceryState, GroceryPriceResult
from dotenv import load_dotenv
load_dotenv()

# Initialize Tavily Tool
tavily_tool = TavilySearchResults(max_results=3, search_depth="basic")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")


class Tool:
    BASE_URL = "https://serpapi.com/search"
    def __init__(self, SERPAPI_API_KEY: str):
        self.api_key = SERPAPI_API_KEY
    @staticmethod
    def search(state: GroceryState) -> GroceryState:
        intent = state.get("intent", "")
        ingredients = state.get("ingredients", [])
        query = state.get("query", "")
        recipe = state.get("recipe_name", [])

        # Only run search if intent is "Recipe"
        if "Recipe" in intent:
            if ingredients:
                search_query = f"{query} with {', '.join(ingredients)}"
            else:
                search_query = query

            results = tavily_tool.run(search_query)

            # Append new result without overwriting
            recipe.append({
                "query": search_query,
                "results": results
            })

        return {
            "recipe_name": recipe
        }

    def get_prize_serpapi(self, ingredient:str) -> List[GroceryPriceResult]:
        params = {
            "engine": "google_shopping",
            "q": ingredient,
            "hl": "en",
            "gl": "in",
            "api_key": self.api_key 
        }

        response = requests.get(self.BASE_URL, params=params) # type: ignore
        data = response.json()
        # print("data", data)
        results = []
        for item in data.get("shopping_results", []):
            print(item)
            try:
                results.append(GroceryPriceResult(
                    product_name=item.get("title", ""),
                    app_name=item.get("source", "Unknown"),
                    price=float(item.get("extracted_price", 0.0)),
                    link=item.get("product_link", "Unknown")
                ))
            except Exception:
                continue
            break
        return results
    
    def update_price_comparison(self, state: GroceryState) -> GroceryState:
        """Update state with price comparison results for all ingredients."""
        state["price_comparison"] = {}
        for ingredient in state["ingredients"]:
            state["price_comparison"][ingredient] = self.get_prize_serpapi(ingredient)
            print("Checking", self.get_prize_serpapi(ingredient))
        return state
    
tool = Tool(SERPAPI_API_KEY)