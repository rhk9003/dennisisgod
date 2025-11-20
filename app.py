import streamlit as st
import requests

# 設定網頁
st.set_page_config(page_title="Dennis AI", page_icon="😎")
st.title("🤖 Dennis AI")

# --- 1. 設定雲端計數器 ---
# 建議修改這裡的 namespace，避免跟別人撞名
COUNTER_NAMESPACE = "dennis_handsome_project" 
COUNTER_KEY = "handsome_clicks"
API_URL = "https://api.counterapi.dev/v1"

def get_global_count():
    try:
        r = requests.get(f"{API_URL}/{COUNTER_NAMESPACE}/{COUNTER_KEY}/")
        if r.status_code == 200:
            return r.json().get("count", 0)
    except:
        pass
    return 0

def increment_global_count():
    try:
        requests.get(f"{API_URL}/{COUNTER_NAMESPACE}/{COUNTER_KEY}/up")
    except:
        pass

# --- 2. 側邊欄顯示 (一開始就讀取雲端數字) ---
current_count = get_global_count()

with st.sidebar:
    st.title("🏆 全網帥氣榜")
    st.metric(
        label="覺得丹尼斯好帥的人次", 
        value=f"{current_count} 人"
    )

# --- 3. 主畫面聊天室 ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "你好，我是智能 AI。"}
    ]

# 顯示歷史訊息
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 接收輸入
if prompt := st.chat_input("在此輸入訊息..."):
    
    # 1. 顯示並儲存【使用者的話】
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. 判斷邏輯
    if prompt == "丹尼斯好帥":
        response = "謝謝我知道 😎"
        
        # 【關鍵修正】：先儲存 AI 的回覆，再去執行計數和重整
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # 更新雲端計數
        increment_global_count()
        
        # 顯示特效
        st.balloons()
        
        # 強制重新整理 (Rerun 會讓程式從頭跑一次，這時上面的歷史訊息就會把剛剛存的「謝謝我知道」顯示出來)
        st.rerun()
        
    else:
        response = "請輸入正確文字：丹尼斯好帥"
        
        # 錯誤時不需要重整，直接顯示並儲存即可
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
