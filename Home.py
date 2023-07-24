import streamlit as st
import numpy as np
import os
st.set_page_config(page_title="Joe's GPT toolbox", page_icon="😊")

st.markdown("# Welcome to Joe's GPT toolbox!👋")

st.markdown(
    """
    在这个小网页中,我将会展示一些我在使用OpenAI API时结合LangChain开发的一些小工具🧰 \n
    - ChatGPT_QA: 一和语言模型进行流式对话 \n
    - ChatPDF: 上传文件，向语言模型进行内容的提问 \n
    - ChatGPT with Tools: 将语言模型与一些工具结合，比如Google，Wikipedia，WolframAlpha等等 \n
    - Python Agent: 一个可以运行Python代码的语言模型 \n
    - Settings: 一些设置，比如OpenAI API的key，Google API的key等等，你无需更改即可使用Joe的所有key \n
    ### 过程中所用到的技术/框架/API来源
    - [Streamlit](https://github.com/streamlit/streamlit) 是一个用于数据科学和机器学习的开源 Python 框架。它提供了一种简单的方式来构建交互式应用程序，使数据科学家和机器学习工程师可以更轻松地将他们的模型展示给其他人。\n
    - [OpenAI API](https://github.com/chatanywhere/GPT_API_free) 支持Models, Embedding, text-davinci, GPT-3.5-Turbo, GPT-3.5-Turbo-16K, GPT-4(免费版不支持), DALLE(免费版不支持), Whisper(免费版不支持)。\n
    - [LangChain](https://docs.langchain.com/docs/) 是一个强大的框架，旨在帮助开发人员使用语言模型构建端到端的应用程序。它提供了一套工具、组件和接口，可简化创建由大型语言模型 (LLM) 和聊天模型提供支持的应用程序的过程。\n
    """
)

if 'openai_api_base' not in st.session_state:
    st.session_state["openai_api_base"] = "https://api.chatanywhere.com.cn/v1"

if 'openai_api_key' not in st.session_state:
    st.session_state["openai_api_key"] = "sk-vNqpgXJo1vbxT0o2ptSoNPOethD2zaSdCN8gh53sPWOUOERl"

if 'serpapi_api_key' not in st.session_state:
    st.session_state["serpapi_api_key"] = "bb1b0a0f24b65e16dbba02f81612706455fe405d34d3df36afc3e8298bb3fccc"

if 'WolframAlpha_api_key' not in st.session_state:
    st.session_state["WolframAlpha_api_key"] = "PK46XL-8QKAATJVJJ"

if 'pinecone_api_key' not in st.session_state:
    st.session_state["pinecone_api_key"] = 'e925f997-8123-4e0d-9c75-b93fa4b78a05'

if 'pinecone_env' not in st.session_state:
    st.session_state["pinecone_env"] = 'asia-southeast1-gcp-free' 

if 'temperature' not in st.session_state:
    st.session_state["temperature"] = 0.8

if 'GOOGLE_CSE_ID' not in st.session_state:
    st.session_state["GOOGLE_CSE_ID"] = "d2d730b968ad74de6"

if 'GOOGLE_API_KEY' not in st.session_state:
    st.session_state["GOOGLE_API_KEY"] = "AIzaSyDAqklhqHg7bf5boWvlrzz-AUFUnYxahmE"

if 'WOLFRAM_ALPHA_APPID' not in st.session_state:
    st.session_state["WOLFRAM_ALPHA_APPID"] = "PK46XL-8QKAATJVJJ"
