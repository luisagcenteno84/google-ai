import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content('tell me the story of philosophy')

print (response.prompt_feedback)
print (response.text)