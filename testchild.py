from openai import OpenAI

# Initialize client with API key
# paste api key
client = OpenAI(api_key="")
#api key nhi h na!!!
messages = []

def completion(message):
    global messages
    messages.append({
        "role": "user",
        "content": message
    })

    chat_completion = client.chat.completions.create(
        model="gpt-4o",   # You can also use "gpt-4.1" or "gpt-3.5-turbo"
        messages=messages
    )

    response = chat_completion.choices[0].message.content

    assistant_message = {
        "role": "assistant",
        "content": response
    }

    messages.append(assistant_message)
    print(f"Jarvis: {response}")


if __name__ == "__main__":
    print("Jarvis: Hi I am Jarvis, How may I help you?\n")
    while True:
        user_question = input("You: ")
        completion(user_question)
