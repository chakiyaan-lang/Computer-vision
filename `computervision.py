import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="VisionForge AI",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for Dark UI Theme
st.markdown("""
    <style>
    /* Dark background styling */
    .stApp {
        background-color: #070d18;
        color: #e8eefc;
    }
    
    /* Card design */
    div[data-testid="stMetricValue"] {
        color: #5264ff;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #5365ff, #714cff);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        width: 100%;
    }
    
    .audit-box {
        background-color: #0d192b;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #1b2b45;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. SIDEBAR
with st.sidebar:
    st.title("✦ VisionForge")
    st.markdown("---")
    
    st.button("⌂  Home")
    st.button("▣  Projects")
    st.button("▤  Datasets")
    st.button("◈  Models")
    st.button("◉  Deployments")
    st.button("♧  Monitoring")
    
    st.markdown("---")
    st.caption("Settings & Help")
    st.button("⚙  Settings")


# 3. MAIN CONTENT AREA
# Top Bar & Header
top_col1, top_col2 = st.columns([3, 1])

with top_col1:
    st.title("Good morning, M Hassaan 👋")
    st.caption("Turn your vision ideas into production-ready models with AI.")

with top_col2:
    st.write("")
    if st.button("+ New Project"):
        st.toast("New project wizard opening...")

st.markdown("---")

# Quick Actions Cards
q1, q2, q3, q4 = st.columns(4)
with q1:
    st.subheader("☁ Upload")
    st.caption("Add images or videos to project.")
with q2:
    st.subheader("✦ AI Audit")
    st.caption("Find imbalance & duplicate images.")
with q3:
    st.subheader("▣ Train")
    st.caption("AI chooses best model settings.")
with q4:
    st.subheader("☁ Deploy")
    st.caption("Deploy and monitor performance.")

st.markdown("---")

# Main Section: Active Project & AI Panel
col_main, col_ai = st.columns([3, 1])

with col_main:
    st.header("Bottle Defect Detection")
    st.caption("Detect damaged bottles in factory production line")
    
    # Progress Pipeline
    st.subheader("Pipeline Progress")
    p1, p2, p3, p4 = st.columns(4)
    p1.success("1. Dataset (Done)")
    p2.success("2. Analysis (Done)")
    p3.info("3. Training (In Progress)")
    p4.warning("4. Evaluation (Pending)")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Two Columns: Dataset + Data Audit
    data_col, audit_col = st.columns(2)
    
    with data_col:
        st.subheader("Dataset Overview")
        st.metric("Total Images", "4,850")
        st.write("● Normal — 3,200 (66%)")
        st.write("● Cracked — 980 (20%)")
        st.write("● Missing Cap — 670 (14%)")
        
    with audit_col:
        st.subheader("AI Data Audit")
        st.error("🔴 Class imbalance detected")
        st.warning("🟡 12 duplicate images found")
        st.info("🔵 8% blurry images")
        
        if st.button("✦ Apply AI Suggestions"):
            st.success("AI Suggestions applied successfully!")

    st.markdown("---")
    
    # Model Training & Comparison Table
    m_train, m_comp = st.columns(2)
    
    with m_train:
        st.subheader("Model Training")
        st.caption("YOLOv8 · Auto Selected")
        st.progress(68)
        st.caption("Epoch 12 / 50 (68%)")
        
        met1, met2, met3 = st.columns(3)
        met1.metric("mAP@0.5", "0.872")
        met2.metric("Precision", "0.91")
        met3.metric("Recall", "0.84")

    with m_comp:
        st.subheader("Model Comparison")
        df = pd.DataFrame({
            "Model": ["YOLOv8", "YOLOv8n", "YOLOv5s", "RT-DETR"],
            "mAP": [0.872, 0.843, 0.821, 0.798],
            "Precision": [0.91, 0.88, 0.85, 0.82],
            "Recall": [0.84, 0.80, 0.76, 0.73]
        })
        st.dataframe(df, hide_index=True, use_container_width=True)

# Right Sidebar: AI Assistant
with col_ai:
    st.subheader("✦ AI Assistant")
    st.info("Hi! I'm your AI ML Engineer. I can analyze datasets, choose models, and diagnose training issues.")
    
    st.write("Quick Prompts:")
    if st.button("✓ Analyze dataset"):
        st.toast("Analyzing dataset...")
    if st.button("✓ Which model to use?"):
        st.toast("Selecting best model...")
    if st.button("✓ Fix class imbalance"):
        st.toast("Fixing imbalance...")
    if st.button("→ Deploy model"):
        st.toast("Deploying...")
        
    user_msg = st.text_input("Ask AI Engineer:", placeholder="Type here...")
    if user_msg:
        st.write(f"**AI Response:** Analyzing '{user_msg}'...")
