from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

HUGGINGFACEHUB_API_KEY = os.getenv("HUGGINGFACE_ACCESS_TOKEN")

question = "Who is Mark Zuckerberg?"

template = """Question: {question}

Answer: Let's think step by step.
"""

prompt = PromptTemplate.from_template(template)

repo_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"

llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    huggingfacehub_api_token=HUGGINGFACEHUB_API_KEY,
)

llm_chain = prompt | llm | StrOutputParser()

response = llm_chain.invoke({"question": question})
print(response)