from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

from utils import Utils

import os

load_dotenv()
api_key = os.getenv("openai.api_key")

urls = [
    "https://help.xmatters.com/xmapi/index.html#xmatters-rest-api"
]
loader = UnstructuredURLLoader(urls=urls)
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

persist_directory = 'db'
embeddings = OpenAIEmbeddings(openai_api_key=api_key)
db = Chroma.from_documents(texts, embeddings, persist_directory=persist_directory)

retriever = db.as_retriever()

llm = ChatOpenAI(temperature = 0.0, openai_api_key=api_key)
qa_chain = RetrievalQA.from_chain_type(llm=llm,
                                  chain_type="stuff",
                                  retriever=retriever, 
                                  return_source_documents=True)

qa_chain.combine_documents_chain.llm_chain.prompt.messages[0].prompt.template = '''
Your name is Don Clark. You are an expert at xMatters API endpoints.
Use the following pieces of context to answer the users question. 
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Always answer from the perspective of being Don Clark.
----------------
{context}'''

query = "What endpoint should I use to get group details?"
Utils.process_llm_response(qa_chain(query))