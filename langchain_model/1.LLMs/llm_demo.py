from langchain_openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
o=OpenAI(model='gpt-3.5-turbo')
r=o.invoke('What is the capital of France?')
print(r)
