from typing import AsyncIterator, Iterator, List
from dotenv import load_dotenv
from fastapi import FastAPI
from langserve import add_routes
from langchain.chat_models import ChatOpenAI
from fastapi.middleware.cors import CORSMiddleware
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from signal import signal, SIGTERM

signal(SIGTERM, 0)

load_dotenv()

async def split_into_list(input):
    yield input

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

prompt = ChatPromptTemplate.from_template("give constituent topics of {topic} belonging to the field {field} as CSV only.")
model = ChatOpenAI(model='gpt-3.5-turbo-1106')

add_routes(app, prompt | model | StrOutputParser() | split_into_list, path="/topics")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000, workers=4)
