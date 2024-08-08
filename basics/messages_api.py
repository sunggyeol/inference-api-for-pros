from openai import OpenAI
import huggingface_hub
import os
from dotenv import load_dotenv
load_dotenv()
HUGGINGFACE_ACCESS_TOKEN = os.getenv("HUGGINGFACE_ACCESS_TOKEN")

# Initialize the client, pointing it to one of the available models
client = OpenAI(
    base_url="https://api-inference.huggingface.co/v1/",
    api_key=HUGGINGFACE_ACCESS_TOKEN,
)
chat_completion = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3-8b-Instruct",
    messages=[
        {"role": "system", "content": "You are a helpful an honest programming assistant."},
        {"role": "user", "content": "Is Rust better than Python?"},
    ],
    stream=True,
    max_tokens=500
)

# iterate and print stream
for message in chat_completion:
    print(message.choices[0].delta.content, end="")
