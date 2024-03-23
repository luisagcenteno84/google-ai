import google.generativeai as genai

model = genai.GenerativeModel('gemini-pro')

prompt = 'give me the origin of life'

safety_settings = {'HARASSMENT': 'block_none'}

response = model.generate_content(prompt, safety_settings=safety_settings)

print(response.text)
print(response.prompt_feedback)