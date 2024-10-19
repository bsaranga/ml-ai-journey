from operator import itemgetter
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

load_dotenv()
vectorstore = FAISS.from_texts(['harrison worked at kensho'], embedding=OpenAIEmbeddings())

retreiver = vectorstore.as_retriever()
template = """Answer the question based only on the following context:
{context}

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
model = ChatOpenAI()

chain = ({"context": retreiver, "question": RunnablePassthrough()}) | prompt | model | StrOutputParser()

for chunk in chain.stream("where did harrison work?"):
    print(chunk, end="", flush=True)