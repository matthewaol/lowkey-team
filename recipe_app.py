from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
app = Flask(__name__)

# Fetch and configure the API key
api_key = os.getenv("API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    raise ValueError("API Key not found.")

@app.route('/')
def home():
    return render_template('index.html')  # Ensure your HTML file is in the templates directory

@app.route('/generate-recipe', methods=['POST'])
def generate_recipe():
    data = request.json
    recipes = []

    for item in data:
        dish_name = item.get('dish_name')
        serving_number = item.get('serving_number', 1)

        # Generate the recipe using the Gemini API
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(
            f'Give a list of ingredients and nutritional information for {dish_name} to serve {serving_number} people.'
            'Give the nutritional information in a dictionary format consisting of the keys being a macronutrient and the value being the quantity (do not format as a range). Format like this: python { "calories": 400, "protein": 30 grams, "carbohydrates": 30 grams, "fat": 15 grams, "saturated fat": 3 grams, "cholesterol": 80 mg, "sodium": 1000 mg, }'
            'Also, please format the ingredients as a string and include the quantities.')
        
        recipes.append({"dish_name": dish_name, "recipe": response.text})

    return jsonify(recipes)

if __name__ == '__main__':
    app.run(debug=True)
