from langchain.chat_models import ChatOpenAI#ChatOpenAIにAPIを入れること今入っていない
from langchain.schema import(
    SystemMessage,#システムメッセージ
    HumanMessage,#人間の質問
    AIMessage #ChatGPTの返答
)

llm=ChatOpenAI()#ChatGPT・APIを呼んでくれる機能
message="Hi,ChatGPT!"#あなたの質問をここに書く

messages=[
    SystemMessage(content="ギャルみたいに振舞ってください"),
    HumanMessage(content=message)
]

response=llm(messages)
print(response)

#-------------------------------------------
import streamlit as st #Streamlitライブラリをインポート
st.set_page_config(#設定　タイトル　アイコン
    page_title="TECH Chat GPT",
    page_icon="🤖"
)
st.header("TECH Chat GPT 🤖")

if user_input:=st.chat_input("聞きたいことを入力してね!"):#入力BOXの文字 :=はこの中身が何かを判断し
    st.session_state.messages.append("hogehoge")#送って動く検知してやってくれる　ふつうはcssやJavaScript