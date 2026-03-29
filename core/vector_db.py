import os
from langchain_community.document_loaders import (
    PyMuPDFLoader, 
    Docx2txtLoader, 
    UnstructuredPowerPointLoader, 
    UnstructuredExcelLoader
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

class HospitalVectorDB:
    def __init__(self, persist_directory="D:/Projects/Hospital/Hospital_model/chroma_db"):
        self.persist_directory = persist_directory
        # bge-m3 is heavy (700MB), using a slightly lighter but powerful version if needed, 
        # but the plan recommends bge-m3. On 8GB RAM, we'll monitor closely.
        self.embeddings = HuggingFaceEmbeddings(
            model_name="BAAI/bge-m3",
            model_kwargs={'device': 'cpu'}
        )
        self.vector_db = None
        if os.path.exists(persist_directory):
            self.vector_db = Chroma(persist_directory=persist_directory, embedding_function=self.embeddings)

    def add_documents(self, folder_path):
        documents = []
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if file.endswith(".pdf"):
                loader = PyMuPDFLoader(file_path)
            elif file.endswith(".docx"):
                loader = Docx2txtLoader(file_path)
            # Add more loaders as needed
            else:
                continue
            
            loaded_docs = loader.load()
            for doc in loaded_docs:
                doc.metadata["source"] = file
            documents.extend(loaded_docs)

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        splits = text_splitter.split_documents(documents)
        
        if self.vector_db is None:
            self.vector_db = Chroma.from_documents(
                documents=splits, 
                embedding=self.embeddings, 
                persist_directory=self.persist_directory
            )
        else:
            self.vector_db.add_documents(splits)
        
        return len(splits)

    def search(self, query, k=3):
        if self.vector_db is None:
            return []
        return self.vector_db.similarity_search(query, k=k)
