import os
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
import shutil


class VectorStoreBuilder:

    def __init__(self, model: str = "zylonai/multilingual-e5-large:latest", persist_dir: str = "./chroma_db"):
        self.model = model
        self.persist_dir = persist_dir
        self.vectorstore = None

    def build(self, chunks) -> Chroma:
        if os.path.exists(self.persist_dir):
            shutil.rmtree(self.persist_dir)

        # show_progress=True больше не поддерживается
        embeddings = OllamaEmbeddings(model=self.model,
                                      base_url="http://localhost:11434")

        self.vectorstore = Chroma.from_documents(documents=chunks,
                                                 embedding=embeddings,
                                                 persist_directory=self.persist_dir)

        return self.vectorstore

    def load(self) -> Chroma:
        if not os.path.exists(self.persist_dir):
            raise FileNotFoundError(
                f"Хранилище не найдено: {self.persist_dir}\n"
                "Сначала создайте его методом build()"
            )

        embeddings = OllamaEmbeddings(
            model=self.model,
            base_url="http://localhost:11434"
        )

        self.vectorstore = Chroma(
            persist_directory=self.persist_dir,
            embedding_function=embeddings
        )

        return self.vectorstore

    def exists(self) -> bool:
        """Проверяет, существует ли сохраненное хранилище"""
        return os.path.exists(self.persist_dir)
