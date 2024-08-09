from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from operator import itemgetter
from dotenv import load_dotenv
import os

load_dotenv()

HUGGINGFACEHUB_API_KEY = os.getenv("HUGGINGFACE_ACCESS_TOKEN")

prompt1 = ChatPromptTemplate.from_template("What city is {person} from?")

prompt2 = ChatPromptTemplate.from_template(
    "What country is the city {city} in? Respond in {language}."
)

repo_id = "meta-llama/Meta-Llama-3-70B-Instruct"

llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    huggingfacehub_api_token=HUGGINGFACEHUB_API_KEY,
)

chain1 = prompt1 | llm | StrOutputParser()


chain2_input = {"city": chain1, "language": "spanish"}
chain2 = prompt2 | llm | StrOutputParser()

country_result = chain2.invoke(chain2_input)
country = country_result.strip()
