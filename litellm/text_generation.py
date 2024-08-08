import os
from dotenv import load_dotenv
from litellm import completion 

load_dotenv()
os.environ["HUGGINGFACE_API_KEY"] = os.getenv("HUGGINGFACE_ACCESS_TOKEN")

messages = [{ "content": "Who is Mark Zuckerberg?","role": "user"}]

response = completion(
    model="huggingface/meta-llama/Meta-Llama-3.1-8B-Instruct",
    messages=messages,
    )

print(response.choices[0].message.content)
