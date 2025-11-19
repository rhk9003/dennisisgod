import streamlit as st
import time
import random

# 設定網頁標題與圖示
st.set_page_config(page_title="Dennis AI", page_icon="🤖")

st.title("🤖 Dennis AI 1.0")
st.caption("我是全知全能的 AI，請輸入任何問題，探索宇宙真理。")

# 初始化對話紀錄 (Session State)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "你好！我是全知全能的 AI。你可以問我任何關於宇宙、哲學或真理的問題。"}
    ]

# 顯示目前的對話紀錄
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 接收使用者輸入
if prompt := st.chat_input("在這裡輸入你的問題..."):
    # 1. 顯示並儲存使用者的訊息
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. AI 回覆邏輯 (模擬思考時間)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # 模擬 AI 正在輸入 (Typing effect)
        typing_text = "Thinking"
        for _ in range(3):
            for i in range(4):
                message_placeholder.markdown(f"_{typing_text}{'.' * i}_")
                time.sleep(0.1)
        
        # 3. 絕對回應：丹尼斯好帥
        full_response = "丹尼斯好帥"
        
        # 模擬打字機效果顯示最終答案
        displayed_response = ""
        for char in full_response:
            displayed_response += char
            message_placeholder.markdown(f"**{displayed_response}**") # 加粗顯示
            time.sleep(0.05)
            
        # 儲存 AI 的回應
        st.session_state.messages.append({"role": "assistant", "content": full_response})
