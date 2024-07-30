from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a useful assistant that classifies text into positive, neurtral or negative"},
        {"role": "user", "content": "I am so happy that I was fired at my job today and my dog died"}
    ],
    temperature=0,
    max_tokens=100,
)


print(response.choices[0].message.content)