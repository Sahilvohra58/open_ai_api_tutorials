## Make sure to install OpenAI Python Module and setup the secret key as an env variable


import os
from openai import OpenAI


# Run the next two lines only if you have a .env file with the OpenAI secret key
# from dotenv import load_dotenv
# load_dotenv()

client = OpenAI()  # Optionally you can provide api key as a arguement here if you have not set it as env var

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  temperature=0,
  max_tokens=200,
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming using 100 words."}
  ]
)

print(completion.choices[0].message.content)