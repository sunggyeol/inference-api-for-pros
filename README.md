# Hugging Face Inference API Playground
An interactive playground to explore and experiment with the Hugging Face Inference API for PRO users. This repository showcases how to leverage the enhanced capabilities available to PRO users, such as increased rate limits and access to state-of-the-art models for various machine learning tasks.

## Overview

The Hugging Face Inference API for PRO users provides several benefits, including:

- **Higher Rate Limits:** Improved API rate limits to support extensive experimentation and prototyping.
- **Access to Exclusive Models:** Use state-of-the-art models for text, image, and audio generation.
- **Ultra-Fast Inference:** Benefit from optimized endpoints for faster model inference.

## Supported Models

This repository includes examples for using some of the most powerful models available to PRO users, such as:

| Model                                  | Endpoint                 | Size         | Context Length | Use                                                |
|----------------------------------------|--------------------------|--------------|----------------|----------------------------------------------------|
| **Meta Llama 3.1 405B Instruct FP8**   | `meta-llama/Meta-Llama-3.1-405B-Instruct-FP8`   | 405B         | 128k tokens    | High-quality multilingual chat model with large context length |
| **Meta Llama 3 Instruct (8B)**         | `meta-llama/Meta-Llama-3-8B-Instruct`       | 8B           | 8k tokens      | One of the best chat models                        |
| **Meta Llama 3 Instruct (70B)**        | `meta-llama/Meta-Llama-3-70B-Instruct`      | 70B          | 8k tokens      | One of the best chat models                        |
| **Mixtral 8x7B Instruct**              | `mistralai/Mixtral-8x7B-Instruct-v0.1` | 45B MOE      | 32k tokens     | Performance comparable to top proprietary models   |
| **Nous Hermes 2 Mixtral 8x7B DPO**     | `NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO` | 45B MOE      | 32k tokens     | Further trained over Mixtral 8x7B MoE              |
| **Zephyr 7B β**                        | `HuggingFaceH4/zephyr-7b-beta`        | 7B           | 4k tokens      | One of the best chat models at the 7B weight       |
| **Llama 2 Chat (7B)**                  | `meta-llama/Llama-2-7b-chat-hf`       | 7B           | 4k tokens      | One of the best conversational models              |
| **Llama 2 Chat (13B)**                 | `meta-llama/Llama-2-13b-chat-hf`      | 13B          | 4k tokens      | One of the best conversational models              |
| **Mistral 7B Instruct v0.2**           | `mistralai/Mistral-7B-Instruct-v0.2`   | 7B           | 4k tokens      | One of the best chat models at the 7B weight       |
| **Code Llama Base (7B)**               | `codellama/CodeLlama-7b-hf`    | 7B           | 4k tokens      | Autocomplete and infill code                       |
| **Code Llama Base (13B)**              | `codellama/CodeLlama-13b-hf`   | 13B          | 4k tokens      | Autocomplete and infill code                       |
| **Code Llama Instruct**                | `codellama/CodeLlama-7b-hf`   | 34B          | 16k tokens     | Conversational code assistant                      |
| **Stable Diffusion XL**                | `stabilityai/stable-diffusion-xl-base-1.0`   | 3B UNet      | -              | Generate images                                    |
| **Bark**                               | `suno/bark`                  | 0.9B         | -              | Text to audio generation                           |

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

### Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

### License

This project is licensed under the MIT License.

## Resources

- [Hugging Face Blog: Inference for PROs](https://huggingface.co/blog/inference-pro)
- [Hugging Face Inference API Documentation](https://huggingface.co/docs/huggingface_hub/main/en/package_reference/inference_client#huggingface_hub.InferenceApi)
- [Hugging Face Substribe to Pro](https://huggingface.co/subscribe/pro)
