from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import json
import os

class RAGSystem:
    def __init__(self, data_dir='./data'):
        self.data_dir = data_dir
        self.embeddings = HuggingFaceEmbeddings()
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        self.vector_store = self._create_vector_store()

    def _create_vector_store(self):
        documents = []
        for filename in os.listdir(self.data_dir):
            if filename.endswith('.json'):
                with open(os.path.join(self.data_dir, filename), 'r') as f:
                    data = json.load(f)
                    for item in data:
                        documents.extend(self.text_splitter.split_text(json.dumps(item)))

        return Chroma.from_texts(documents, self.embeddings)

    def retrieve(self, query, k=3):
        return self.vector_store.similarity_search(query, k=k)