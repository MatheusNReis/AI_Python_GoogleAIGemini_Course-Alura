!pip install google-genai

import os
from google.colab import userdata

# Retrieving the API key from Colab's secrets folder in an environment variable
os.environ['GOOGLE_API_KEY'] = userdata.get('GOOGLE_API_KEY') # os.environ is used to create an environment variable
                                                              # userdata is used to get the API key

from google import genai
# Creating a client object, used to interact with a service
client = genai.Client()

for model in client.models.list():
  print(model.name)

modelo = 'gemini-2.0-flash'

resposta = client.models.generate_content(model = modelo,
                                          contents = 'Quem é a empresa por trás dos modelos do Gemini?')

resposta.text


chat = client.chats.create(model = modelo)

resposta = chat.send_message("Oi, tudo bem?")

resposta.text


resposta = chat.send_message("Você é um assistente virtual e sempre responde de forma sucinta. O que é inteligência artificial?")

resposta.text


from google.genai import types

#sytem instruction - Set the how the assistent must respond
chat_config = types.GenerateContentConfig(
    system_instruction = "Você é um assistente pessoal e sempre responde de foma sucinta.",
)

chat = client.chats.create(model = modelo, config = chat_config)


resposta = chat.send_message("O que é computação quântica?")

resposta.text


chat.get_history()

#Observe the variables "text" and "role" related


prompt = input("Esperando prompt: ")

while prompt != "fim":
  resposta = chat.send_message(prompt)
  print("Resposta:", resposta.text)
  print("\n")
  prompt = input("Esperando prompt: ")


#sytem instruction - Set the how the assistent must respond
chat_config_2 = types.GenerateContentConfig(
    system_instruction = "Você é um assistente pessoal e sempre responde de foma muito sarcástica.",
)

chat_2 = client.chats.create(model = modelo, config = chat_config_2)


resposta = chat_2.send_message("O que é computação quântica?")

resposta.text
