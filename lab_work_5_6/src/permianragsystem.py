from langchain_chroma import Chroma
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# from langchain_classic.chains.retrieval_qa.base import RetrievalQA
# from langchain_classic.prompts import PromptTemplate


class PermianRAGSystem:

    def __init__(self, vectorstore: Chroma, llm_model: str = "gemma3:4b", k: int = 5):
        self.vectorstore: Chroma = vectorstore
        self.llm = OllamaLLM(model=llm_model,
                             base_url="http://localhost:11434",
                             temperature=0.4,
                             top_p=0.9,
                             num_predict=512)
        self.prompt_template = """
You are an expert in paleontology and the Permian period.
Use ONLY the provided context from Wikipedia articles to answer the question.
If the answer is not in the context, say "This information is not available in the provided documents."
Provide an answer in Russian!
Context: {context}
Question: {question}
Detailed Answer:"""
        self.k = k
        self.retriever = vectorstore.as_retriever(search_kwargs={"k": self.k})
        self.prompt = ChatPromptTemplate.from_template(self.prompt_template)
        # LCEL (LangChain Expression Language)
        self.rag_chain = ({"context": self.retriever, "question": RunnablePassthrough()} | self.prompt | self.llm | StrOutputParser())

        # self.prompt = PromptTemplate(template=self.prompt_template,
        #                              input_variables=["context", "question"])

        # self.qa_chain = RetrievalQA.from_chain_type(llm=self.llm,
        #                                             chain_type="stuff",
        #                                             retriever=vectorstore.as_retriever(search_kwargs={"k": 4}),
        #                                             return_source_documents=True,
        #                                             chain_type_kwargs={"prompt": self.prompt},
        #                                             verbose=False)

    def search_in_vectorstore(self, question: str) -> dict:

        docs_with_scores = self.vectorstore.similarity_search_with_score(question, self.k)

        return {
            "question": question,
            "docs": sorted([
                {
                    "id": doc.id,
                    "source": doc.metadata.get('source', 'Unknown'),
                    "content": doc.page_content[:300],
                    "score": score
                } for doc, score in docs_with_scores], key=lambda x: x['score'], reverse=True)
        }

    def answer_question(self, question: str) -> dict:
        # result = self.qa_chain.invoke({"query": question})

        # Получаем контекст для источников
        context_docs = self.retriever.invoke(question)

        # Полный ответ
        answer = self.rag_chain.invoke(question)

        return {
                "question": question,
                "answer": answer,
                "sources": [
                    {
                        "title": doc.metadata.get('source', 'Unknown'),
                        "content": doc.page_content[:300],
                        "metadata": doc.metadata
                    } for doc in context_docs]
                }

    def steam_answer_question(self, question: str):

        for chunk in self.rag_chain.stream(question):
            yield chunk