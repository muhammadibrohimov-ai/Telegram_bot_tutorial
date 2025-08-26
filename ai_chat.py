import google.generativeai as genai

from environs import Env

env = Env()
env.read_env()

API_TOKEN = env.str("API_KEY")

genai.configure(api_key=API_TOKEN)

model = genai.GenerativeModel("gemini-2.0-flash")

chat = model.start_chat()

def chatting(message):
    responce = chat.send_message(message)
    return responce.text