import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

os.getenv("OPENAI_API_KEY")
prompt = ChatPromptTemplate.from_template("Tell me a short joke about {topic}")
model = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

chain = {"topic": RunnablePassthrough()} | prompt | model | output_parser

# streaming
for chunk in chain.stream("ice cream"):
    print(chunk, end="", flush=True)
    
# batching
""" result = chain.batch(["ice cream", "spaghetti", "dumplings"])
print(result) """