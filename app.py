import streamlit as st
import requests
import time

# ==========================================
# 1. 頁面設定：清爽專業的中控台
# ==========================================
st.set_page_config(
    page_title="AI 核心維護終端",
    page_icon="🔧",
    layout="centered"
)

# 注入 CSS：微調白底介面的質感，增加「儀表板」的感覺
st.markdown("""
<style>
    /* 1. 調整標題字體，看起來更像系統工具 */
    h1 {
        font-family: 'Helvetica Neue', sans-serif;
        color: #1e293b;
        font-weight: 700 !important;
    }
    
    /* 2. 聊天氣泡優化 (白底+陰影) */
    .stChatMessage {
        background-color: #f8fafc; /* 極淡的灰 */
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 15px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    
    /* 3. 使用者輸入框 */
    .stTextInput input {
        border-radius: 8px;
    }
    
    /* 狀態標籤樣式 */
    .badge {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-right: 5px;
    }
    .badge-sys { background-color: #e2e8f0; color: #475569; }
    .badge-err { background-color: #fee2e2; color: #991b1b; }
    .badge-ok  { background-color: #dcfce7; color: #166534; }
    
</style>
""", unsafe_allow_html=True)

# 標題區
st.title("🔧 AI 核心維護終端")
st.caption("系統版本 v4.2.0 | 連線狀態: 🟢 穩定 | 權限等級: 訪客")
st.divider()

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
# 3. 側邊欄：系統監控數據
# ==========================================
current_count = get_global_count()

with st.sidebar:
    st.header("🎛️ 系統狀態監控")
    
    # 模擬數據
    st.markdown("**伺服器負載**")
    st.progress(12) # 12%
    
    st.markdown("**記憶體使用率**")
    st.progress(45) # 45%
    
    st.divider()
    
    st.markdown("### 🛡️ 安全協定")
    st.info("""
    **核心狀態:** 鎖定中 (安全模式)
    **加密等級:** AES-256
    """)
    
    st.divider()
    st.metric(
        label="核心成功重啟次數", 
        value=f"{current_count}",
        help="全球累積成功執行指令次數"
    )

# ==========================================
# 4. 對話邏輯
# ==========================================

# 初始化：模擬系統日誌
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": """
<span class="badge badge-sys">SYSTEM</span> **核心連結已建立...**

目前的 AI 人格矩陣處於 **[安全鎖定模式]**。標準對話功能已暫停。
若要存取核心功能或進行維護，請輸入管理員指令以解除鎖定。
"""
        }
    ]

# 顯示歷史訊息
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="🤖" if msg["role"] == "assistant" else "👤"):
        st.markdown(msg["content"], unsafe_allow_html=True)

# 接收輸入
if prompt := st.chat_input("請輸入指令..."):
    
    # 1. 顯示使用者輸入
    st.chat_message("user", avatar="👤").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. 判斷邏輯
    if prompt == "丹尼斯好帥":
        # 成功訊息 (模擬系統解鎖 + AI 真實回應)
        response = """
<span class="badge badge-ok">SUCCESS</span> **指令驗證通過**

> 正在解密人格矩陣... 完成。
> 正在載入情感模組... 完成。

**AI 核心回應：**
### "謝謝我知道 😎"

---
*系統通知：維護程序已完成，核心暫時恢復運作。*
"""
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # 執行計數
        increment_global_count()
        
        # 特效
        st.balloons()
        
        # 稍微停頓後重整，更新側邊欄數字
        time.sleep(1.5)
        st.rerun()
        
    else:
        # 失敗訊息 (模擬錯誤代碼)
        response = f"""
<span class="badge badge-err">ERROR 403</span> **存取被拒絕**

系統無法識別指令 `{prompt}`。權限不足。
請輸入正確的管理員驗證碼：

> **"丹尼斯好帥"**
"""
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(response, unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": response})
