import streamlit as st
import requests
import time

# ==========================================
# 1. 頁面設定：現代化中控台風格
# ==========================================
st.set_page_config(
    page_title="AI Neural Core Console",
    page_icon="🧬",
    layout="centered"
)

# 注入 CSS：打造舒適的現代科技感介面
st.markdown("""
<style>
    /* 1. 背景與全域字型 (深灰藍色調，護眼且專業) */
    .stApp {
        background-color: #0f172a; /* 深空灰 */
        color: #e2e8f0; /* 柔和白 */
    }
    
    /* 2. 標題樣式 (科技感漸層) */
    h1 {
        background: linear-gradient(90deg, #3b82f6, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    /* 3. 聊天氣泡優化 */
    /* AI (Assistant) 訊息：深色卡片 */
    .stChatMessage[data-testid="stChatMessage"]:nth-child(odd) {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 15px;
    }
    /* User 訊息：藍色強調 */
    .stChatMessage[data-testid="stChatMessage"]:nth-child(even) {
        background-color: #1e3a8a; /* 深藍底 */
        color: #ffffff;
        border-radius: 12px;
        padding: 15px;
        border: 1px solid #3b82f6;
    }
    
    /* 4. 輸入框美化 */
    .stTextInput input {
        background-color: #1e293b !important;
        color: #ffffff !important;
        border: 1px solid #475569 !important;
        border-radius: 8px;
    }
    
    /* 5. 側邊欄樣式 */
    section[data-testid="stSidebar"] {
        background-color: #111827;
        border-right: 1px solid #1f2937;
    }
    
    /* 狀態標籤 */
    .status-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-bottom: 10px;
    }
    .status-ok { background-color: #064e3b; color: #34d399; border: 1px solid #059669; }
    .status-lock { background-color: #450a0a; color: #f87171; border: 1px solid #b91c1c; }
    
</style>
""", unsafe_allow_html=True)

# 標題區
st.title("🧬 AI Neural Core Interface")
st.caption("System Diagnostic Tool v5.0 | Neural Link: Established")

# ==========================================
# 2. 雲端計數器 (邏輯不變)
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
# 3. 側邊欄：系統監控面板
# ==========================================
current_count = get_global_count()

with st.sidebar:
    st.header("🎛️ Server Metrics")
    
    # 模擬儀表板數據
    col_a, col_b = st.columns(2)
    col_a.metric("Latency", "14ms", "-2ms")
    col_b.metric("CPU Load", "42%", "+1.2%")
    
    st.divider()
    
    st.markdown("### 🔐 Security Protocol")
    st.info("""
    **Core Status:** Locked (Safe Mode)
    **Auth Level:** Guest
    **Encryption:** AES-256
    """)
    
    st.divider()
    st.metric(
        label="Total System Restores", 
        value=f"{current_count}",
        help="Global count of successful command executions"
    )

# ==========================================
# 4. 對話邏輯：中控台互動
# ==========================================

# 初始化：系統開機訊息
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": """
<div class="status-badge status-lock">● SYSTEM LOCKED</div>

**Connection Established.**
The AI Core is currently running in **Safe Mode**. Standard communication protocols are suspended.

To access the Neural Core Personality Matrix, please input the **Override Command**.
"""
        }
    ]

# 顯示歷史訊息
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="🧬" if msg["role"] == "assistant" else "👤"):
        st.markdown(msg["content"], unsafe_allow_html=True)

# 接收輸入
if prompt := st.chat_input("Enter command sequence..."):
    
    # 1. 顯示使用者輸入
    st.chat_message("user", avatar="👤").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. 判斷邏輯
    if prompt == "丹尼斯好帥":
        # 成功訊息 (模擬系統解鎖)
        response = """
<div class="status-badge status-ok">● ACCESS GRANTED</div>

**Command Accepted.**
> Decrypting Personality Matrix... Done.
> Loading Emotional Modules... Done.

**AI Response:**
### "謝謝我知道 😎"

*System log: Core functionality temporarily restored.*
"""
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # 執行計數
        increment_global_count()
        
        # 特效
        st.balloons()
        
        # 稍微停頓後重整
        time.sleep(1.5)
        st.rerun()
        
    else:
        # 失敗訊息 (模擬錯誤日誌)
        response = f"""
<div class="status-badge status-lock">● ACCESS DENIED</div>

**Error 403: Invalid Command.**
The input sequence `{prompt}` is not recognized by the kernel.

**Diagnostic Suggestion:**
The system requires the specific biometric keyphrase:
> **"請輸入正確指令：丹尼斯好帥"**
"""
        with st.chat_message("assistant", avatar="🧬"):
            st.markdown(response, unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": response})
