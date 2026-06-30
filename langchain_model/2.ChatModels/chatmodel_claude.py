from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

m = ChatAnthropic(model='claude-3-5-sonnet-20241022')

r = model.invoke('What is the capital of India')

print(r.content)