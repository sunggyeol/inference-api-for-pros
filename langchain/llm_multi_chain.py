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

repo_id = "NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO"

model = HuggingFaceEndpoint(
    repo_id=repo_id,
    huggingfacehub_api_token=HUGGINGFACEHUB_API_KEY,
)

chain1 = prompt1 | model | StrOutputParser()

chain2 = (
    {"city": chain1, "language": itemgetter("language")}
    | prompt2
    | model
    | StrOutputParser()
)

output = chain2.invoke({"person": "obama", "language": "spanish"})

print(output)