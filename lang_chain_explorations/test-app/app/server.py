from dotenv import load_dotenv
from fastapi import FastAPI
from langserve import add_routes
from langchain.chat_models import ChatOpenAI
from fastapi.middleware.cors import CORSMiddleware
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import BaseTransformOutputParser
from signal import signal, SIGTERM

signal(SIGTERM, 0)

load_dotenv()

class StrCollectParser(BaseTransformOutputParser[str]):
    """OutputParser that parses LLMResult into the top likely string."""

    buffer: str = ""

    @classmethod
    def is_lc_serializable(cls) -> bool:
        """Return whether this class is serializable."""
        return True

    @property
    def _type(self) -> str:
        """Return the output parser type for serialization."""
        return "default"

    def parse(self, text: str) -> str:
        """Returns the input text with no changes."""
        buffer += text
        
        split = buffer.split(',')
        
        if (len(split) > 0):
            buffer = ""
            for k in split:
                return k

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

add_routes(app, prompt | model | StrCollectParser(), path="/topics")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000, workers=4)
