from dotenv import load_dotenv
from fastapi import FastAPI
from langserve import add_routes
from langchain.chat_models import ChatOpenAI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

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

# Edit this to add the chain you want to add
add_routes(app, ChatOpenAI(), path="/openai")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
