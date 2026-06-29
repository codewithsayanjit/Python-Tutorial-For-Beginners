from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)