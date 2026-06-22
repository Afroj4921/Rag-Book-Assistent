from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

#load pdf
loader = PyPDFLoader("document loaders/GRU.pdf")
docs = loader.load()


#split imto chunks
splitters = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 100
)

chunks = splitters.split_documents(docs)

#create the embeddings
embedding_model = MistralAIEmbeddings()

#store into chroma
vectorstore = Chroma.from_documents(
    documents = chunks,
    embedding = embedding_model,
    persist_directory="Chroma_db"

)
