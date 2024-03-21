from langchain_community.llms import Ollama

# create large language model using 'phi' model
llm = Ollama(model="phi")

# invoke the model
response = llm.invoke("Tell me a programming joke")

# print the response
print(response)