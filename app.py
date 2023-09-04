"""Simple LLM Chat App
"""


import streamlit as st

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage


st.set_page_config(page_title="Simple chat with LLM", page_icon=":robot:")
st.header("Simple chat with LLM")


chat_model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

if "sessionMessages" not in st.session_state:
    st.session_state.sessionMessages = [
        SystemMessage(content="You are a helpful assustant."),
    ]


def get_user_text():
    """Get Human Text or Question"""
    input_text = st.text_input("You: ", key="input_text")
    return input_text


def get_AI_Answer(user_text):
    """Get AI answer"""
    st.session_state.sessionMessages.append(HumanMessage(content=user_text))
    ai_answer = chat_model(st.session_state.sessionMessages)
    st.session_state.sessionMessages.append(ai_answer)
    return ai_answer.content


user_text = get_user_text()
submit = st.button("Submit")

if submit:
    ai_answer_text = get_AI_Answer(user_text)
    st.subheader("AI")
    st.write(ai_answer_text)
