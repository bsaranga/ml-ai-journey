from dotenv import load_dotenv
from fastapi import FastAPI
from langserve import add_routes
from langchain.chat_models import ChatOpenAI

load_dotenv()

app = FastAPI(
    title="LangChain Test Server",
    version="1.0",
    description="A simple server to checkout Langchain capabilities",
)

# Edit this to add the chain you want to add
add_routes(app, ChatOpenAI(), path="/openai")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
