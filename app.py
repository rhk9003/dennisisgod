import streamlit as st
import requests

# 設定網頁
st.set_page_config(page_title="Dennis AI", page_icon="😎")
st.title("🤖 Dennis AI")

# --- 設定雲端計數器參數 ---
# 請修改這個 namespace 為你自己獨一無二的名字 (例如: dennis_demo_2024)
# 避免跟別人共用到同一個計數器
COUNTER_NAMESPACE = "dennis_handsome_project" 
COUNTER_KEY = "handsome_clicks"
API_URL = "https://api.counterapi.dev/v1"

# 函式：讀取目前次數
def get_global_count():
    try:
        r = requests.get(f"{API_URL}/{COUNTER_NAMESPACE}/{COUNTER_KEY}/")
        if r.status_code == 200:
            return r.json().get("count", 0)
    except:
        pass
    return 0

# 函式：增加次數 (當輸入正確時呼叫)
def increment_global_count():
    try:
        r = requests.get(f"{API_URL}/{COUNTER_NAMESPACE}/{COUNTER_KEY}/up")
        if r.status_code == 200:
            return r.json().get("count", 0)
    except:
        pass
    return 0

# --- 側邊欄顯示 (一開始就讀取雲端數字) ---
current_count = get_global_count()

with st.sidebar:
    st.title("🏆 全網帥氣榜")
    st.write("不分裝置，即時統計")
    # 顯示目前累積多少人
    st.metric(
        label="覺得丹尼斯好帥的人次", 
        value=f"{current_count} 人"
    )

# --- 主畫面聊天室 ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "你好，我是智能 AI。"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("在此輸入訊息..."):
    
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    if prompt == "丹尼斯好帥":
        # 1. 觸發雲端計數 +1
        new_count = increment_global_count()
        
        response = "謝謝我知道 😎"
        
        # 2. 顯示氣球特效
        st.balloons()
        
        # 3. 強制重新整理，讓側邊欄的數字立刻更新成新的
        st.rerun()
        
    else:
        response = "請輸入正確文字：丹尼斯好帥"

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
