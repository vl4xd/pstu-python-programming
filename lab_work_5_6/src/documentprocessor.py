from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

class DocumentProcessor:

    def __init__(self, documents_dir: str, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.documents_dir = documents_dir
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.documents = []
        self.chunks = []

    def load_and_chunk(self) -> dict:
        loader = DirectoryLoader(
            self.documents_dir,
            glob="**/*.txt",
            loader_cls=TextLoader,
            loader_kwargs={'encoding': 'utf-8'}
        )

        self.documents = loader.load()

        splitter = RecursiveCharacterTextSplitter(chunk_size=self.chunk_size,
                                                  chunk_overlap=self.chunk_overlap,
                                                  length_function=len,
                                                  separators=["\n\n", "\n", ". ", " ", ""])

        self.chunks = splitter.split_documents(self.documents)

        return {
            'num_documents': len(self.documents),
            'num_chunks': len(self.chunks),
            'total_chars': sum(len(doc.page_content) for doc in self.documents),
            'avg_chunk_size': sum(len(chunk.page_content) for chunk in self.chunks) / len(self.chunks)
            }