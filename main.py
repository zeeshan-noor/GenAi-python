from langchain_openai import OpenAI #type: ignore
from dotenv import load_dotenv
import os
load_dotenv()

llm = OpenAI(openapi_key=os.getenv('OPENAI_API_KEY'))

prompt = "Translate the following English language into German:'Hello, How are you doing now !!' "
response = llm.invoke(prompt)
print(response)