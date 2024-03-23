import google.generativeai as genai

model = genai.GenerativeModel('gemini-pro')

chat = model.start_chat(history=[])

prompt = 'explain to a child how is a corgi dog different from other dogs'

print(f"Token count: {model.count_tokens(prompt)}")

response = chat.send_message(prompt, stream=True)



for chunk in response:
    print(chunk.text)
    print("_"*80)

#print(response.text)



#print(chat.history)