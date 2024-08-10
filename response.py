import openai

api_key =  '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'

openai.api_key = api_key

user_input = input("You: ")

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=user_input,
    max_tokens=100
)

print("AI:", response.choices[0].text.strip())