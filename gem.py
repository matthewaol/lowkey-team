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

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(f"Give a list of ingredients and nutritional information for {dish_name}")
print(response.text)