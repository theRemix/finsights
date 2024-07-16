from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain.indexes.vectorstore import VectorstoreIndexCreator
from langchain_openai import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
)

loader = CSVLoader(file_path="./data.csv")
data = loader.load()
embedding = OpenAIEmbeddings()
index = VectorstoreIndexCreator(embedding=embedding).from_loaders([loader])


def query(q):
    return index.query(q, llm=llm)
