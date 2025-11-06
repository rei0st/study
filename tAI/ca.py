import streamlit as st #Streamlitライブラリをインポート
from langchain.chat_models import ChatOpenAI#ChatOpenAIにAPIを入れること今入っていない
from langchain.schema import(SystemMessage,HumanMessage,AIMessage) #メッセージ関連import

def main():
    lim=ChatOpenAI(temperature=0)#ChatOpenAIのインスタンスを作成、温度パラメーターを0に設定

    st.set_page_config(
        page_title="TECH Chat GPT",
        page_icon="🤖"
    )
    st.header("TECK Chat GPT 🤖")

#チャットの履歴を初期化
    if "messages" not in st.session_state:#セッション状態にmessagesがなければ
        st.session_state.messages=[
            SystemMessage(content="なんでも聞いてね!")#システムメッセージを初期メッセージとして設定
        ]

#ユーザーの入力を監視
    if user_input:=st.chat_input("聞きたいことを入力してね!"):#ユーザーの入力を受け取り
        st.session_state.messages.append(HumanMessage(content=user_input))#入力をHumanMessageとして追加
        with st.spinner("ChatGPT is typing..."):#処置中のスピナーを表示
            response=lim(st.session_state.messages)#チャット履歴をもとにレスポンスを生成
        st.session_state.messages.append(AIMessage(content=response.content))#レスポンスをAIMessageとして追加

#チャットの履歴の表示
messages=st.session_state.get("messages",[])#セッション状態からmessagesを取得、なければ空のリスト
for messages in messages:#メッセージリストをループ
    if isinstance(message,AIMessage):#メッセージがAIMessageの場合　isinstanceなんの種類のメッセージなの？見分けてるpython
        with st.chat_message("assistant"):#アシスタントとしてメッセージを表示
            st.markdown(message.content)
    elif isinstance(message,HumanMessage):#メッセージがHumanmessageの場合
        with st.chat_message("user"):#ユーザーとしてメッセージを表示
            st.markdown(message.content)
    else:#それ以外の場合、SystemMessageとしてみなす
        st.write(f"System message:{message.content}")#システムメッセージを表示

if __name__ == "__main__":
    main()#main関数を実行