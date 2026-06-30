from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

l = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    huggingfacehub_api_token="hf",
    task="text-generation"
)

m = ChatHuggingFace(llm=l)

print(m.invoke("What is the capital of India?").content)