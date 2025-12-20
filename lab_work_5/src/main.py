import gradio as gr

from vectorstorebuilder import VectorStoreBuilder
from permianragsystem import PermianRAGSystem


vectorstorebuilder = VectorStoreBuilder('zylonai/multilingual-e5-large:latest')
vectorstore = vectorstorebuilder.load()
rag_system = PermianRAGSystem(vectorstore, 'gemma3:4b')


def rag_interface(question: str):
    """Gradio interface reusing existing format_response function"""
    if not question.strip():
        yield "Пожалуйста, введите вопрос."
        return

    response_start = f"<h3>❓Вопрос:</h3><p>{question}</p><h3>📝Ответ:</h3><p>"
    answer = ""

    for token in rag_system.steam_answer_question(question):
        answer += token
        yield response_start + answer + "</p>"


if __name__ == "__main__":

    # Create Gradio interface with streaming support
    demo = gr.Interface(
        fn=rag_interface,
        inputs=gr.Textbox(
            label="Задайте вопрос о Пермском периоде",
            placeholder="Сколько продолжался Пермский период и каковы его точные даты начала и окончания?",
            lines=2,
        ),
        outputs=gr.Markdown(label="Answer"),
        title="🦕 RAG система: Пермский период",
        # description="",
        examples=[
            "Сколько продолжался Пермский период и каковы его точные даты начала и окончания?",
            "Каким был климат на Земле во время Пермского периода? Опишите основные тенденции.",
            "Какие основные группы растений существовали на суше в Пермском периоде?",
        ],
        flagging_mode="never",
    )

    demo.queue().launch(share=True)
