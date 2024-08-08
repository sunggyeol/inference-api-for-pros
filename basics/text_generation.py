import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
load_dotenv()
HUGGINGFACE_ACCESS_TOKEN = os.getenv("HUGGINGFACE_ACCESS_TOKEN")

client = InferenceClient(model="meta-llama/Meta-Llama-3-8b-Instruct", token=HUGGINGFACE_ACCESS_TOKEN)

output = client.text_generation("Who is Mark Zuckerberg?")
print(output)

