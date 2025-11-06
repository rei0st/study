import streamlit as st

st.set_page_config(
    page_title="TECH Chat GPT",
    page_icon="🤖"
)

# セッション状態の初期化
if "messages" not in st.session_state:
    st.session_state.messages = []

st.header("TECH Chat GPT 🤖")

if user_input := st.chat_input("聞きたいことを入力してね!"):
    # メッセージをディクショナリ形式で追加
    st.session_state.messages.append({"role": "user", "content": user_input})