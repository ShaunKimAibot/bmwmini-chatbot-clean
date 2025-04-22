from app.config import retriever, llm
from langchain.schema import HumanMessage, SystemMessage

def generate_response_with_images(query: str, docs):
    # 문맥 생성
    context = "\n\n".join([doc.page_content for doc in docs])
    messages = [
        SystemMessage(content="당신은 BMW Mini Cooper 매뉴얼 전문가입니다."),
        HumanMessage(content=f"질문: {query}\n\n참고 내용:\n{context}")
    ]
    response = llm.invoke(messages)
    return {
        "answer": response.content,
        "image_urls": []  # 이미지 연동 시 여기에 URL 넣을 수 있어요
    }

def get_response(query: str):
    docs = retriever.invoke(query)
    return generate_response_with_images(query, docs)
