import gradio as gr

from vectorstorebuilder import VectorStoreBuilder
from permianragsystem import PermianRAGSystem


def rag_interface(question: str):
    """Gradio interface reusing existing format_response function"""
    if not question.strip():
        yield "Please enter a question."
        return

    response_start = f"**Question:** {question}\n\n**Answer:** "
    answer = ""

    # Stream the answer progressively
    for token in rag_system.steam_answer_question(question):
        answer += token
        yield response_start + answer

    # Use existing formatting function for final response
    # yield format_response(question, answer, documents)

if __name__ == "__main__":
    vectorstorebuilder = VectorStoreBuilder('zylonai/multilingual-e5-large:latest')
    vectorstore = vectorstorebuilder.load()
    rag_system = PermianRAGSystem(vectorstore, 'gemma3:4b')

    # Create Gradio interface with streaming support
    demo = gr.Interface(
        fn=rag_interface,
        inputs=gr.Textbox(
            label="Задайте вопрос о Пермском периоде",
            placeholder="How do if-else statements work in Python?",
            lines=2,
        ),
        outputs=gr.Markdown(label="Answer"),
        title="RAG система: Пермский период",
        # description="",
        examples=[
            "Сколько продолжался Пермский период и каковы его точные даты начала и окончания?",
            "Каким был климат на Земле во время Пермского периода? Опишите основные тенденции.",
            "Какие основные группы растений существовали на суше в Пермском периоде?",
        ],
        flagging_mode="never",
    )

    demo.queue().launch(share=True)