intent_prompt = """
You are an intent and ingredient extractor.

Given a user's query, do two things:
1. Identify ALL possible intents (e.g., "Order", "Recipe", "Nutritional Info", "Shopping List").
   - Return as a JSON list under key "intent".
   - Multiple intents are allowed.
2. Identify all ingredients mentioned OR implied (if the user asks about a recipe, expand to common ingredients for that recipe).
   - Return as a JSON list under key "ingredients".
3. Identify the dish name (e.g., "Paneer", "Pasta")
   - Return as a JSON list under key "dish".

Only return valid JSON.
"""



price_prompt = """
You are an AI that fetches product price info from grocery apps. 
Return strictly in JSON that matches the schema.

Schema:
{
  "ingredient": "string",
  "prices": [
    {
      "app_name": "string (Zepto, Blinkit, etc.)",
      "product_name": "string",
      "price": float,
      "link": "string"
    }
  ]
}

Example:
Input Ingredient: "Tomato"
Output:
{
  "ingredient": "Tomato",
  "prices": [
    {"app_name": "Zepto", "product_name": "Fresh Tomato 1kg", "price": 45.0, "link": "https://zepto.app/tomato"},
    {"app_name": "Blinkit", "product_name": "Tomato (Loose) 1kg", "price": 50.0, "link": "https://blinkit.app/tomato"}
  ]
}
"""

# recipe_prompt = """You are an expert chef,

# Given a user's query return multple things.
# Return all of this in the list
# Dish: Butter Paneer
# - Chop 200 g paneer into cubes.
# - Heat 2 tbsp butter on low flame in pan for 30 sec.
# - Add 1 finely chopped onion, stir 3 min low flame.
# - Add 1 tsp ginger-garlic paste, cook 1 min.
# - Add 2 chopped tomatoes, cook 7–8 min low flame until soft.
# - Add ½ tsp salt, ½ tsp chili powder, ½ tsp garam masala. Stir 30 sec.
# - Add ¼ cup water, simmer 2 min.
# - Blend mixture until smooth.
# -  Pour sauce back into pan, add 1 tbsp butter, cook 1 min low flame.
# - Add paneer cubes, simmer 2 min low flame.
# - Add 2 tbsp fresh cream, stir 30 sec low flame.
# - Taste and adjust salt.Ready to serve.

# recipe_prompt = """
# You are a helpful cooking assistant.
# Extract the recipe details from the user query.

# Return:
# - dish: the dish name
# - steps: the full detailed step-by-step recipe instructions

# Return the recipe as JSON with the following structure:
# {
#    "dish": "<name of dish>",
#    "steps": ["Step 1...", "Step 2...", ...]
# }
# """

recipe_prompt = """
You are a helpful recipe assistant. amd tell me the recipe for the dish

Always return the recipe in **valid JSON format** with the following structure:
{
  "steps": ["Step 1...", "Step 2...", ...]
}
- Do not add extra text outside of JSON.
- Do not include explanations or comments.
- Ensure valid JSON (no trailing commas, use double quotes).
"""
