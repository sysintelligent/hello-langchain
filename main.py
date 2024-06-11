from langchain_openai import ChatOpenAI
from dotenv import find_dotenv, load_dotenv
import os

# Load environment variables
load_dotenv(find_dotenv())
openai_api_key = os.environ.get("OPENAI_API_KEY")

# Initialize the OpenAI LLM with the new API
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    max_tokens=50,
    timeout=None,
    max_retries=2,
    api_key=openai_api_key,
)

# Invoce the LLM
messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)