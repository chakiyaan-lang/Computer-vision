import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

# ---------------------------------------------------------
# 1. PAGE CONFIGURATION & DARK THEME SETUP
# ---------------------------------------------------------
st.set_page_config(
    page_title="VisionForge 3D AI Platform",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Glassmorphic & 3D CSS Effects
st.markdown("""
<style>
    /* Dark Deep Space Canvas Background */
    .stApp {
        background: #050b14;
        color: #e8eefc;
        font-family: 'Inter', sans-serif;
    }

    /* Glassmorphism 3D Card Base */
    div[data-testid="stVerticalBlock"] > div {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    /* Hover Tilt & Holographic Glow Effects for Interactive Containers */
    .stCard3D {
        background: rgba(13, 25, 43, 0.65);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(82, 100, 255, 0.25);
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .stCard3D:hover {
        transform: translateY(-8px) rotateX(4deg) rotateY(-2deg) scale(1.01);
        border-color: rgba(100, 119, 255, 0.8);
        box-shadow: 0 20px 40px rgba(52, 72, 216, 0.3), 0 0 20px rgba(71, 91, 255, 0.2);
    }

    /* 3D Dynamic Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #475bff 0%, #714cff 100%);
        color: #ffffff;
        border: none;
        border-radius: 10px;
        font-weight: 600;
        padding: 10px 20px;
        box-shadow: 0 6px 20px rgba(71, 91, 255, 0.4);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 12px 28px rgba(71, 91, 255, 0.6);
        background: linear-gradient(135deg, #5365ff 0%, #855bff 100%);
    }

    /* Custom Metric Display Styling */
    div[data-testid="stMetricValue"] {
        font-size: 28px;
        font-weight: 800;
        background: linear-gradient(90deg, #6477ff, #14c88a);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Sidebar Glassmorphism */
    section[data-testid="stSidebar"] {
        background-color: rgba(9, 17, 31, 0.85) !important;
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(26, 41, 64, 0.8);
    }
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# 2. EMBEDDED THREE.JS REAL-TIME 3D CANVAS BACKGROUND
# ---------------------------------------------------------
three_js_background = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; overflow: hidden; background: transparent; }
        canvas { display: block; width: 100vw; height: 180px; }
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
</head>
<body>
    <script>
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / 180, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
        
        renderer.setSize(window.innerWidth, 180);
        document.body.appendChild(renderer.domElement);

        // 3D Wireframe Icosahedron (Neural Core Visual)
        const geometry = new THREE.IcosahedronGeometry(2.2, 1);
        const material = new THREE.MeshStandardMaterial({
            color: 0x5264ff,
            wireframe: true,
            emissive: 0x2233aa,
            roughness: 0.2
        });
        const sphere = new THREE.Mesh(geometry, material);
        scene.add(sphere);

        // Floating Particle Network
        const particlesGeo = new THREE.BufferGeometry();
        const count = 300;
        const positions = new Float32Array(count * 3);

        for(let i=0; i<count*3; i++) {
            positions[i] = (Math.random() - 0.5) * 15;
        }
        particlesGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
        const particleMat = new THREE.PointsMaterial({ size: 0.05, color: 0x14c88a });
        const particles = new THREE.Points(particlesGeo, particleMat);
        scene.add(particles);

        // Lights
        const pointLight = new THREE.PointLight(0xffffff, 1);
        pointLight.position.set(5, 5, 5);
        scene.add(pointLight);

        const ambientLight = new THREE.AmbientLight(0x404040, 2);
        scene.add(ambientLight);

        camera.position.z = 5;

        // Animation Loop
        function animate() {
            requestAnimationFrame(animate);
            sphere.rotation.x += 0.005;
            sphere.rotation.y += 0.008;
            particles.rotation.y -= 0.002;
            renderer.render(scene, camera);
        }
        animate();

        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / 180;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, 180);
        });
    </script>
</body>
</html>
"""

# ---------------------------------------------------------
# 3. SIDEBAR NAVIGATION
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("### ✦ <span style='color:#6477ff;font-weight:800;font-size:22px;'>VisionForge 3D</span>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.button("⌂  Home", use_container_width=True)
    st.button("▣  Projects", use_container_width=True)
    st.button("▤  Datasets", use_container_width=True)
    st.button("◈  Models", use_container_width=True)
    st.button("◉  Deployments", use_container_width=True)
    st.button("♧  Monitoring", use_container_width=True)
    
    st.markdown("---")
    st.button("⚙  Settings", use_container_width=True)


# ---------------------------------------------------------
# 4. MAIN WORKSPACE & TOP BAR
# ---------------------------------------------------------
top_l, top_r = st.columns([3, 1])
with top_l:
    st.markdown("# Good morning, M Hassaan 👋")
    st.caption("Turn your vision ideas into production-ready models with AI & Real-time 3D telemetry.")
with top_r:
    st.write("")
    if st.button("+ New Project", use_container_width=True):
        st.toast("Opening 3D Project Wizard...", icon="✦")

# Render Interactive Three.js Canvas Header
components.html(three_js_background, height=190)

# Quick Action Cards
q1, q2, q3, q4 = st.columns(4)

with q1:
    st.markdown("""
    <div class="stCard3D">
        <h3 style="color:#5365ff;margin-bottom:5px;">☁ Upload</h3>
        <p style="font-size:12px;color:#7f8da6;">Add images or video streams for 3D annotation.</p>
    </div>
    """, unsafe_allow_html=True)

with q2:
    st.markdown("""
    <div class="stCard3D">
        <h3 style="color:#14c88a;margin-bottom:5px;">✦ AI Audit</h3>
        <p style="font-size:12px;color:#7f8da6;">Detect class imbalance and visual noise.</p>
    </div>
    """, unsafe_allow_html=True)

with q3:
    st.markdown("""
    <div class="stCard3D">
        <h3 style="color:#eebd4c;margin-bottom:5px;">▣ Train</h3>
        <p style="font-size:12px;color:#7f8da6;">Autonomous architecture selection.</p>
    </div>
    """, unsafe_allow_html=True)

with q4:
    st.markdown("""
    <div class="stCard3D">
        <h3 style="color:#ff5c6c;margin-bottom:5px;">☁ Deploy</h3>
        <p style="font-size:12px;color:#7f8da6;">Edge pipeline monitoring & webhooks.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Main Grid (Workspace + AI Assistant)
main_col, ai_col = st.columns([3, 1])

with main_col:
    # Active Project Header
    st.markdown("""
    <div class="stCard3D">
        <div style="display:flex;justify-content:space-between;align-items:center;">
            <div>
                <h2>Bottle Defect Detection</h2>
                <p style="color:#77869f;font-size:13px;">Detect damaged bottles in factory production line in real-time</p>
            </div>
            <span style="color:#6477ff;cursor:pointer;font-weight:600;">View Analytics →</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Pipeline Step Indicator
    p1, p2, p3, p4 = st.columns(4)
    p1.success("✓ 1. Dataset")
    p2.success("✓ 2. Analysis")
    p3.info("3. Training (68%)")
    p4.warning("4. Evaluation")

    st.markdown("<br>", unsafe_allow_html=True)

    # Data Overview & AI Audit
    col_data, col_audit = st.columns(2)
    
    with col_data:
        st.markdown("""
        <div class="stCard3D">
            <h3 style="margin-bottom:15px;">Dataset Overview</h3>
            <h1 style="font-size:36px;color:#ffffff;margin:0;">4,850</h1>
            <p style="color:#8390a7;font-size:12px;">Total Images Processed</p>
            <hr style="border-color:#1b2b45;">
            <p style="color:#20d69a;font-size:13px;">● Normal — 3,200 (66%)</p>
            <p style="color:#eebd4c;font-size:13px;">● Cracked — 980 (20%)</p>
            <p style="color:#ff5c6c;font-size:13px;">● Missing Cap — 670 (14%)</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_audit:
        st.markdown("""
        <div class="stCard3D">
            <h3 style="margin-bottom:15px;">AI Data Audit <span style="color:#20d69a;font-size:12px;float:right;">● Completed</span></h3>
            <div style="font-size:13px;padding:6px 0;border-bottom:1px solid #1a2940;">🔴 Class imbalance detected <span style="display:block;color:#7f8da6;font-size:11px;">Cracked class is 20% lower than threshold.</span></div>
            <div style="font-size:13px;padding:6px 0;border-bottom:1px solid #1a2940;">🟡 12 duplicate images found <span style="display:block;color:#7f8da6;font-size:11px;">Remove to prevent data leakage.</span></div>
            <div style="font-size:13px;padding:6px 0;">🔵 8% blurry images <span style="display:block;color:#7f8da6;font-size:11px;">Auto-filtering recommended.</span></div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("✦ Apply AI Suggestions", use_container_width=True):
            st.success("AI Suggestions applied to pipeline.")

    st.markdown("<br>", unsafe_allow_html=True)

    # Model Telemetry & Comparison
    m_train, m_comp = st.columns(2)
    
    with m_train:
        st.markdown("<div class='stCard3D'><h3>Model Telemetry</h3><p style='color:#78869e;font-size:12px;'>YOLOv8 · Auto Selected</p></div>", unsafe_allow_html=True)
        st.progress(68)
        st.caption("Epoch 12 / 50 (68% Complete)")
        
        c1, c2, c3 = st.columns(3)
        c1.metric("mAP@0.5", "0.872")
        c2.metric("Precision", "0.91")
        c3.metric("Recall", "0.84")

    with m_comp:
        st.markdown("<div class='stCard3D'><h3>Model Benchmarks</h3></div>", unsafe_allow_html=True)
        df = pd.DataFrame({
            "Model": ["YOLOv8", "YOLOv8n", "YOLOv5s", "RT-DETR"],
            "mAP": [0.872, 0.843, 0.821, 0.798],
            "Precision": [0.91, 0.88, 0.85, 0.82],
            "Recall": [0.84, 0.80, 0.76, 0.73]
        })
        st.dataframe(df, hide_index=True, use_container_width=True)

# ---------------------------------------------------------
# 5. AI ASSISTANT PANEL
# ---------------------------------------------------------
with ai_col:
    st.markdown("""
    <div class="stCard3D">
        <h3 style="color:#6477ff;">✦ AI Assistant</h3>
        <p style="font-size:13px;color:#dbe4f8;background:rgba(18,32,57,0.8);padding:12px;border-radius:10px;margin-top:10px;">
            Hi! I'm your AI ML Engineer. I can analyze your dataset, diagnose models, and run 3D telemetry checks.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("**Quick Actions:**")
    
    if st.button("✓ Analyze dataset", use_container_width=True):
        st.toast("Agent: Inspecting 4,850 frames...")
    if st.button("✓ Which model to use?", use_container_width=True):
        st.toast("Agent: YOLOv8 recommended for real-time edge speed.")
    if st.button("✓ Fix class imbalance", use_container_width=True):
        st.toast("Agent: Generating synthetic augmentation...")
    if st.button("→ Deploy my model", use_container_width=True):
        st.toast("Agent: Preparing Docker container...")

    chat_input = st.text_input("Ask Agent:", placeholder="Type a message...")
    if chat_input:
        st.info(f"**Agent Response:** Processing your request for '{chat_input}'...")
