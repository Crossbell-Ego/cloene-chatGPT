from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
import os
from langchain.memory import ConversationBufferMemory


def get_chat_response(prompt, memory, openai_api_key):
    model = ChatOpenAI(model="gpt-4o-mini", openai_api_key=openai_api_key)
    chain = ConversationChain(llm=model, memory=memory)
    response = chain.invoke({"input": prompt})
    return response["response"]

# memory = ConversationBufferMemory(return_messages=True)
# print(get_chat_response("明天八點叫我寫作業?",memory,os.getenv("OPENAAI_API_KEY")))
# print(get_chat_response("什麼時候要叫我寫作業?",memory,os.getenv("OPENAAI_API_KEY")))