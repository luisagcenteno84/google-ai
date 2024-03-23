import PIL.Image
import google.generativeai as genai


#img = PIL.Image.open("image\IMG_0427.jpeg") #drawing
img = PIL.Image.open("image\IMG_0438.jpeg") # Buongiorno! I am in Firenze, Italia. 🇮🇹
#img = PIL.Image.open("image\IMG_0450.jpeg") #St Mark's Square
#img = PIL.Image.open("image\IMG_4885.jpeg")# flights

model = genai.GenerativeModel('gemini-pro-vision')

response = model.generate_content(['write a brief and engaging blog post using this picture?',img]) 

print(response.text)