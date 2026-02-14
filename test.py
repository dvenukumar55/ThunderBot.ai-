
from groq import Groq

client = Groq(
    api_key="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"
)

while True:
    user_input = input("you: ")

    if user_input.lower() in ["quit", "exit", "bye"]:
        break

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        print("ThunderBot.ai:", response.choices[0].message.content)

    except Exception as e:
        print("Error:", e)
