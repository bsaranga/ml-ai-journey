from typing import Iterator, List
from dotenv import load_dotenv
from fastapi import FastAPI
from langserve import add_routes
from langchain.chat_models import ChatOpenAI
from fastapi.middleware.cors import CORSMiddleware
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import BaseCumulativeTransformOutputParser
from langchain.prompts.chat import SystemMessagePromptTemplate, HumanMessagePromptTemplate
from signal import signal, SIGTERM

signal(SIGTERM, 0)

load_dotenv()

class MyParser(BaseCumulativeTransformOutputParser):
    def parse(self, text: str) -> str:
        print(text)
        return {"topics": text.split(', ')}

app = FastAPI(
    title="LangChain Test Server",
    version="1.0",
    description="A simple server to checkout Langchain capabilities",
)

origins = ['http://localhost:5173', 'http://127.0.0.1:5173']

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

system_message = SystemMessagePromptTemplate.from_template("you are a helpful assistant that return lists of items as comma separated values. each item should be concise as much as possible.")
human_message = HumanMessagePromptTemplate.from_template("give constituent topics of {topic} belonging to {field}.")
prompt = ChatPromptTemplate.from_messages([system_message, human_message])

model = ChatOpenAI(model='gpt-4-0613')

add_routes(app, prompt | model | MyParser(), path="/topics")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000, workers=4)
