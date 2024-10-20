import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Fetch the API key from environment variables
api_key = os.getenv("API_KEY")

if api_key:
    print(f"API Key is: {api_key}")
else:
    print("API Key not found.")


genai.configure(api_key=os.environ["API_KEY"])

dish_name = "orange chicken"
serving_number = 2

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(f'Give a list of ingredients and nutritional information for {dish_name} to serve {serving_number} people.'    
                                   'Give the nutrional information in a dictionary format consisting of the keys being a macronutrient and the value being the quantity.' 
                                   'Also, please format the ingredients as a string and include the quantities')
print(response.text)