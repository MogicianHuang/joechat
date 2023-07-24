import streamlit as st

st.write("## 基本设置⚙️")



api_base_input = st.text_input(label="转发HOST",
                           placeholder=f"请在这儿输入您的转发HOST, 默认为https://api.chatanywhere.cn")

api_key_input = st.text_input(label="API KEY",
                            placeholder="请在这儿输入您的API KEY, 默认为Joe的API KEY")

serpapi_key_input = st.text_input(label="SERPAPI KEY",placeholder="请在这儿输入您的SERPAPI KEY, 默认为Joe的SERPAPI KEY")

wolframalpha_key_input = st.text_input(label="WolframAlpha KEY",placeholder="请在这儿输入您的WolframAlpha KEY, 默认为Joe的WolframAlpha KEY")

pinecone_api_key_input = st.text_input(label="Pinecone API KEY",placeholder="请在这儿输入您的Pinecone API KEY, 默认为Joe的Pinecone API KEY")
pinecone_env_input = st.text_input(label="Pinecone ENV",placeholder="请在这儿输入您的Pinecone ENV, 默认为Joe的Pinecone ENV")

button = st.button("完成设置", key="predict")

if api_base_input:
    st.session_state["openai_api_base"] = api_base_input
    st.write(f"已经将转发HOST设置为{st.session_state['openai_api_base']}")


if api_key_input:
    st.session_state["openai_api_key"] = api_key_input
    st.write(f"已经将API KEY设置为{st.session_state['openai_api_key']}")

if serpapi_key_input:
    st.session_state["serpapi_api_key"] = serpapi_key_input
    st.write(f"已经将SERPAPI KEY设置为{st.session_state['serpapi_api_key']}")

if wolframalpha_key_input:
    st.session_state["WolframAlpha_api_key"] = wolframalpha_key_input
    st.write(f"已经将WolframAlpha KEY设置为{st.session_state['WolframAlpha_api_key']}")

if pinecone_api_key_input:
    st.session_state["pinecone_api_key"] = pinecone_api_key_input
    st.write(f"已经将Pinecone API KEY设置为{st.session_state['pinecone_api_key']}")

if pinecone_env_input:
    st.session_state["pinecone_env"] = pinecone_env_input
    st.write(f"已经将Pinecone ENV设置为{st.session_state['pinecone_env']}")



