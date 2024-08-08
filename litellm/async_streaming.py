import logging
from litellm import acompletion
import asyncio
import os
import traceback
from dotenv import load_dotenv

load_dotenv()
os.environ["HUGGINGFACE_API_KEY"] = os.getenv("HUGGINGFACE_ACCESS_TOKEN")

logging.getLogger("LiteLLM").setLevel(logging.ERROR)

async def completion_call():
    try:        
        response = await acompletion(
            model="huggingface/meta-llama/Meta-Llama-3.1-8B-Instruct",
            messages=[{"content": "Write a poem about Mark Zuckerberg.", "role": "user"}],
            stream=True
        )
        async for chunk in response:
            content = chunk.choices[0].delta.content
            if content is not None:
                if content == "<|eot_id|>":
                    break
                print(content, end='')
        print()
    except Exception as e:
        print(f"Error occurred: {traceback.format_exc()}")

asyncio.run(completion_call())
