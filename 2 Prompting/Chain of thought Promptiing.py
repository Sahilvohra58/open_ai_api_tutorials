from openai import OpenAI

client = OpenAI()



print("Chain of thought prompting with few shot learning\n\n")
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1."},
        {"role": "assistant", "content": "Adding all the odd numbers (9, 15, 1) gives 25. The answer is False."},

        {"role": "user", "content": "The odd numbers in this group add up to an even number: 17,  10, 19, 4, 8, 12, 24."},
        {"role": "assistant", "content": " Adding all the odd numbers (17, 19) gives 36. The answer is True."},

        {"role": "user", "content": "The odd numbers in this group add up to an even number: 16,  11, 14, 4, 8, 13, 24."},
        {"role": "assistant", "content": " Adding all the odd numbers (11, 13) gives 24. The answer is True."},

        {"role": "user", "content": "The odd numbers in this group add up to an even number: 17,  9, 10, 12, 13, 4, 2."},
        {"role": "assistant", "content": "Adding all the odd numbers (17, 9, 13) gives 39. The answer is False."},

        {"role": "user", "content": "The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1."},
        
    ],
    temperature=0,
    max_tokens=100,
)
print(response.choices[0].message.content)


print("\n\nZero Shot chainof thought prompting\n\n")

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "I went to the market and bought 10 apples. I gave 2 apples to the neighbor and 2 to the repairman. I then went and bought 5 more apples and ate 1. How many apples did I remain with?"},
        {"role": "assistant", "content": "Let's think step by step."},
    ],
    temperature=0,
    max_tokens=100,
)
print(response.choices[0].message.content)