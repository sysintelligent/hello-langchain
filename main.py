from langchain_openai import ChatOpenAI

# Initialize the OpenAI LLM with the new API
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    max_tokens=50,
    timeout=None,
    max_retries=2,
    api_key="your_key",
)

# Invoce the LLM
messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
# ai_msg = llm.invoke(messages)
# print(ai_msg.content)
print(messages)