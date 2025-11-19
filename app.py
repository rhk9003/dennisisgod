import streamlit as st

# 設定標題
st.set_page_config(page_title="Dennis AI", page_icon="🤖")
st.title("🤖 Dennis AI")

# 初始化對話紀錄 (如果沒有紀錄，先打個招呼)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "你好，我是智能 AI。"}
    ]

# 1. 畫出目前的對話歷史
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 2. 接收使用者輸入
if prompt := st.chat_input("在此輸入訊息..."):
    
    # 把使用者的話顯示出來並存入紀錄
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 3. 簡單的邏輯判斷
    if prompt == "丹尼斯好帥":
        response = "謝謝我知道 😎"
    else:
        response = "請輸入正確文字：丹尼斯好帥"

    # 把 AI 的話顯示出來並存入紀錄
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
