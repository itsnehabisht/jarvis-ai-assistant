from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key= os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def ask_ai(prompt):

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    
    except Exception as e:
        return f"An error occurred while processing your request: {str(e)}"