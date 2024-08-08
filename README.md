# Hugging Face Inference API Playground
An interactive playground to explore and experiment with the Hugging Face Inference API for PRO users. This repository showcases how to leverage the enhanced capabilities available to PRO users, such as increased rate limits and access to state-of-the-art models for various machine learning tasks.

## Overview

The Hugging Face Inference API for PRO users provides several benefits, including:

- **Higher Rate Limits:** Improved API rate limits to support extensive experimentation and prototyping.
- **Access to Exclusive Models:** Use state-of-the-art models for text, image, and audio generation.
- **Ultra-Fast Inference:** Benefit from optimized endpoints for faster model inference.

## Supported Models

This repository includes examples for using some of the most powerful models available to PRO users, such as:

- **Meta Llama 3.1 405B:** High-quality multilingual chat model.
- **Code Llama:** For code completion and infilling tasks.
- **Stable Diffusion XL:** Image generation using diffusion models.
- **Bark:** Text-to-audio generation.

## Getting Started

### Prerequisites

- A Hugging Face PRO subscription to access the exclusive features and models.
- Python 3.7 or later installed on your system.
- `huggingface_hub` Python library for easy API integration.

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/sunggyeol/huggingface-playground.git
   cd huggingface-playground
   ```

2. Install the necessary Python packages:

   ```bash
   pip install huggingface_hub
   ```

### Authentication

To use the PRO features, you'll need to authenticate with your PRO account token:

- Obtain your token from the Hugging Face account settings.
- Authenticate using the `huggingface_hub` library:

  ```python
  from huggingface_hub import InferenceClient

  # Log in using your token
  client = InferenceClient(token="YOUR_PRO_TOKEN")
  ```

### Usage Examples

#### Text Generation with Meta Llama

```python
from huggingface_hub import InferenceClient

client = InferenceClient(
    "meta-llama/Meta-Llama-3-8B-Instruct",
    token="hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
)

for message in client.chat_completion(
	messages=[{"role": "user", "content": "What is the capital of France?"}],
	max_tokens=500,
	stream=True,
):
    print(message.choices[0].delta.content, end="")
```

#### Image Generation with Stable Diffusion XL

```python
import requests

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": "Astronaut riding a horse",
})
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))
```

### Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

### License

This project is licensed under the MIT License.

## Resources

- [Hugging Face Inference API](https://huggingface.co/docs/inference-api/serverless)
- [Hugging Face Blog: Inference for PROs](https://huggingface.co/blog/inference-pro)
- [Hugging Face Inference API Documentation](https://huggingface.co/docs/huggingface_hub/main/en/package_reference/inference_client#huggingface_hub.InferenceApi)
- [Hugging Face Substribe to Pro](https://huggingface.co/subscribe/pro)
