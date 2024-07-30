from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "A whatpu is a small, furry animal native to Tanzania. An example of a sentence that uses the word whatpu is:"},
        {"role": "assistant", "content": "We were traveling in Africa and we saw these very cute whatpus."},
        {"role": "user", "content": "To do a farduddle means to jump up and down really fast. An example of a sentence that uses the word farduddle is:"},
    ],
    temperature=0,
    max_tokens=100,
)
print(response.choices[0].message.content)