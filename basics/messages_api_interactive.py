from openai import OpenAI
import huggingface_hub
import os
from dotenv import load_dotenv
load_dotenv()
HUGGINGFACE_ACCESS_TOKEN = os.getenv("HUGGINGFACE_ACCESS_TOKEN")

# Initialize the client with Hugging Face's API
client = OpenAI(
    base_url="https://api-inference.huggingface.co/v1/",
    api_key=HUGGINGFACE_ACCESS_TOKEN,
)

# Initialize chat history
messages = [
    {"role": "system", "content": "You are a helpful and honest programming assistant."}
]

def chat_with_model():
    while True:
        # Get user input
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'q']:
            print("Exiting chat...")
            break

        # Add user message to chat history
        messages.append({"role": "user", "content": user_input})

        # Send the message to the model
        chat_completion = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3-8b-Instruct",
            messages=messages,
            stream=True,
            max_tokens=500
        )

        # Print the model's response
        response = ""
        for message in chat_completion:
            response += message.choices[0].delta.content

        # Print the full response
        print(f"Model: {response.strip()}")

        # Add model's response to chat history
        messages.append({"role": "assistant", "content": response.strip()})

if __name__ == "__main__":
    chat_with_model()
