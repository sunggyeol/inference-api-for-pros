from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
load_dotenv()

HUGGINGFACE_ACCESS_TOKEN = os.getenv("HUGGINGFACE_ACCESS_TOKEN")

sdxl = InferenceClient(model="stabilityai/stable-diffusion-xl-base-1.0", token=HUGGINGFACE_ACCESS_TOKEN)
image = sdxl.text_to_image(
    "Mark Zuckerberg is the CEO of Meta Platforms, Inc. He is a billionaire and a philanthropist.",
    guidance_scale=9,
)

image.save("image.png")