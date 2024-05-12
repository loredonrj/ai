import os
from dotenv import load_dotenv

import openai
import langchain
from langchain_community.llms import OpenAI
from langchain_openai import OpenAI

load_dotenv()

my_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0, openai_api_key=my_key)
text = "What is AI?"
print(llm.invoke(text))