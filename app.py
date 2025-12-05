import streamlit as st
import requests
import time

# ==========================================
# 1. 頁面設定：偽裝成系統後台
# ==========================================
st.set_page_config(
    page_title="System Kernel Console",
    page_icon="🔧",
    layout="centered"
)

# 注入 CSS 讓介面看起來像駭客終端機
st.markdown("""
<style>
    /* 全局背景與字體 */
    .stApp {
        background-color: #0e1117;
        color: #00ff00;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* 聊天氣泡樣式重寫 */
    .stChatMessage {
        background-color: #0e1117 !important;
        border: 1px solid #333;
        border-radius: 5px;
    }
    
    /* 使用者輸入框 */
    .stTextInput input {
        color: #00ff00 !important;
        background-color: #1c1c1c !important;
        border: 1px solid #00ff00 !important;
    }
    
    /* 標題樣式 */
    h1 {
        color: #00ff00 !important;
        text-shadow: 0 0 10px #00ff00;
        font-size: 2.5rem !important;
    }
    
    /* 側邊欄 */
    section[data-testid="stSidebar"] {
        background-color: #111;
        border-right: 1px solid #333;
    }
</style>
""", unsafe_allow_html=True)

st.title("🖥️ AI Core Maintenance")
st.caption("v4.2.0-beta | Connection: Secure | Latency: 12ms")
st.markdown("---")

# ==========================================
# 2. 雲端計數器 (維持原邏輯)
# ==========================================
COUNTER_NAMESPACE = "dennis_handsome_project" 
COUNTER_KEY = "handsome_clicks"
API_URL = "https://api.counterapi.dev/v1"

def get_global_count():
    try:
        r = requests.get(f"{API_URL}/{COUNTER_NAMESPACE}/{COUNTER_KEY}/", timeout=2)
        if r.status_code == 200:
            return r.json().get("count", 0)
    except:
        pass
    return 0

def increment_global_count():
    try:
        requests.get(f"{API_URL}/{COUNTER_NAMESPACE}/{COUNTER_KEY}/up", timeout=2)
    except:
        pass

# ==========================================
# 3. 側邊欄：系統狀態監控
# ==========================================
current_count = get_global_count()

with st.sidebar:
    st.header("📊 SYSTEM STATUS")
    st.markdown("---")
    st.code(f"""
[OK] CPU Usage..... 12%
[OK] Memory........ 4GB
[OK] Network....... Stable
    """, language="bash")
    
    st.markdown("### 🏆 Protocol Executions")
    st.metric(
        label="核心修復次數 (Global Count)", 
        value=f"{current_count}",
        delta="Stable"
    )
    st.info("System running in protected mode.")

# ==========================================
# 4. 終端機對話邏輯
# ==========================================

# 初始化：顯示像是系統開機的日誌
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": """
```bash
> SYSTEM_BOOT_SEQUENCE_INIT...
> LOADING_KERNEL... OK
> CHECKING_PERMISSIONS... LOCKED 🔒
```
⚠️ **ALERT**: AI Core functions are currently **SUSPENDED**.
Administrator intervention required.

Please input the **Root Access Command** to restore functionality.
"""
        }
    ]

# 顯示歷史訊息
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 接收輸入 (Prompt)
if prompt := st.chat_input("Enter system command..."):
    
    # 1. 顯示使用者輸入 (模擬指令輸入)
    st.chat_message("user").markdown(f"```bash\n$ {prompt}\n```")
    st.session_state.messages.append({"role": "user", "content": f"```bash\n$ {prompt}\n```"})

    # 2. 判斷邏輯
    if prompt == "丹尼斯好帥":
        # 成功訊息 (偽裝成系統修復報告)
        response = """
```diff
+ ACCESS GRANTED.
+ DECRYPTING CORE... 100%
+ OPTIMIZATION COMPLETE.
```
✅ **SYSTEM RESTORED**: 
Acknowledgement received: **"謝謝我知道 😎"**
"""
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # 執行計數
        increment_global_count()
        
        # 特效：氣球代表「系統恢復慶祝」
        st.balloons()
        
        # 強制重整以更新側邊欄數據
        time.sleep(1) # 稍微停頓讓使用者看到訊息
        st.rerun()
        
    else:
        # 失敗訊息 (偽裝成嚴重錯誤)
        response = f"""
```diff
- ERROR 403: INVALID COMMAND SYNTAX.
- COMMAND '{prompt}' NOT RECOGNIZED.
```
🚫 **ACCESS DENIED**:
System integrity check failed. 
Required input protocol: **"請輸入正確指令：丹尼斯好帥"**
"""
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
