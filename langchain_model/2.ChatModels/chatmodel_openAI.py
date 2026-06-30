from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
# temp:- 0:- code terms , 1.5-2.0 : story telling 
m = ChatOpenAI(model="gpt-4",temperature=0,max_completion_tokens=100)
r=m.invoke("What is the capital of France?")
print(r)


