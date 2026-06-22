from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

data = PyPDFLoader("document loaders/GRU.pdf")

docs = data.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 10
)

chunks = splitter.split_documents(docs)


#semantic splitting - splits the whole thing according to the sentences and thefinds the similariy between the embeding and merthem accordingly
#this is in preparation not useable yet


# 1 page is 1 document
print(len(chunks))
print(chunks[0])