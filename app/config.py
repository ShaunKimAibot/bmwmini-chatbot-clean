# 환경변수가 필요할 경우 여기에 추가
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores.supabase import SupabaseVectorStore
from supabase import create_client
import os

# 환경 변수 (Render에 설정 필요)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)

llm = ChatOpenAI(
    model_name="gpt-4o",
    temperature=0.2,
    api_key=OPENAI_API_KEY
)

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=1536,
    api_key=OPENAI_API_KEY
)

vectorstore = SupabaseVectorStore(
    client=client,
    embedding=embeddings,
    table_name="embeddings",
    query_name="match_embeddings"
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
