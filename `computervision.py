import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np

# ---------------------------------------------------------
# 1. PAGE CONFIGURATION & DARK THEME SETUP
# ---------------------------------------------------------
st.set_page_config(
    page_title="VisionForge 3D AI Platform",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Glassmorphic CSS Styling
st.markdown("""
<style>
    .stApp {
        background: #050b14;
        color: #e8eefc;
        font-family: 'Inter', sans-serif;
    }
    .stCard3D {
        background: rgba(13, 25, 43, 0.65);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(82, 100, 255, 0.25);
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        transition: all 0.3s ease;
        margin-bottom: 15px;
    }
    .stCard3D:hover {
        border-color: rgba(100, 119, 255, 0.8);
        box-shadow: 0 15px 35px rgba(52, 72, 216, 0.3);
    }
    .stButton > button {
        background: linear-gradient(135deg, #475bff 0%, #714cff 100%);
        color: #ffffff;
        border: none;
        border-radius: 10px;
        font-weight: 600;
        padding: 10px 20px;
        box-shadow: 0 6px 20px rgba(71, 91, 255, 0.3);
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #5365ff 0%, #855bff 100%);
    }
    div[data-testid="stMetricValue"] {
        font-size: 26px;
        font-weight: 800;
        background: linear-gradient(90deg, #6477ff, #14c88a);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    section[data-testid="stSidebar"] {
        background-color: rgba(9, 17, 31, 0.85) !important;
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(26, 41, 64, 0.8);
    }
</style>
""", unsafe_allow_html=True)

# Three.js 3D Background Component
THREE_JS_HTML = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; overflow: hidden; background: transparent; }
        canvas { display: block; width: 100vw; height: 130px; }
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
</head>
<body>
    <script>
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / 130, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
        
        renderer.setSize(window.innerWidth, 130);
        document.body.appendChild(renderer.domElement);

        const geometry = new THREE.IcosahedronGeometry(2, 1);
        const material = new THREE.MeshStandardMaterial({
            color: 0x5264ff,
            wireframe: true,
            emissive: 0x112288
        });
        const sphere = new THREE.Mesh(geometry, material);
        scene.add(sphere);

        const particlesGeo = new THREE.BufferGeometry();
        const count = 200;
        const positions = new Float32Array(count * 3);
        for(let i=0; i<count*3; i++) {
            positions[i] = (Math.random() - 0.5) * 12;
        }
        particlesGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
        const particleMat = new THREE.PointsMaterial({ size: 0.04, color: 0x14c88a });
        const particles = new THREE.Points(particlesGeo, particleMat);
        scene.add(particles);

        const pointLight = new THREE.PointLight(0xffffff, 1);
        pointLight.position.set(5, 5, 5);
        scene.add(pointLight);
        scene.add(new THREE.AmbientLight(0x404040, 2));

        camera.position.z = 4.5;

        function animate() {
            requestAnimationFrame(animate);
            sphere.rotation.x += 0.004;
            sphere.rotation.y += 0.006;
            particles.rotation.y -= 0.001;
            renderer.render(scene, camera);
        }
        animate();
    </script>
</body>
</html>
"""

# ---------------------------------------------------------
# 2. MODULE FUNCTIONS (Clean Separation)
# ---------------------------------------------------------

def render_dashboard():
    top_l, top_r = st.columns([3, 1])
    with top_l:
        st.markdown("# Welcome back, M Hassaan 👋")
        st.caption("Autonomous Computer Vision Engine — Multi-Module Control Center")
    with top_r:
        st.write("")
        if st.button("+ New Vision Project", key="btn_new_proj", use_container_width=True):
            st.toast("Opening Project Wizard...", icon="✦")

    components.html(THREE_JS_HTML, height=140)

    q1, q2, q3, q4 = st.columns(4)
    q1.metric("Images Processed", "4,850", "+12% this week")
    q2.metric("Dataset Quality Score", "84%", "+5% auto-fixed")
    q3.metric("Current Best mAP", "0.872", "YOLOv8")
    q4.metric("Active Endpoint", "99.9%", "Edge Engine")

    st.markdown("<br>", unsafe_allow_html=True)
    main_col, ai_col = st.columns([3, 1])

    with main_col:
        st.markdown("""
        <div class="stCard3D">
            <h3>Bottle Defect Detection Pipeline</h3>
            <p style="color:#77869f;font-size:13px;">Real-time inspection of factory manufacturing lines using edge vision.</p>
        </div>
        """, unsafe_allow_html=True)

        p1, p2, p3, p4 = st.columns(4)
        p1.success("✓ 1. Data Health")
        p2.success("✓ 2. Auto-Augment")
        p3.info("3. Model Training")
        p4.warning("4. Stress Testing")

        st.markdown("<br>", unsafe_allow_html=True)
        c_a, c_b = st.columns(2)
        with c_a:
            st.markdown("""
            <div class="stCard3D">
                <h4>Dataset Breakdown</h4>
                <p style="color:#20d69a;margin-top:10px;">● Normal Bottles — 3,200 (66%)</p>
                <p style="color:#eebd4c;">● Cracked Bodies — 980 (20%)</p>
                <p style="color:#ff5c6c;">● Missing Caps — 670 (14%)</p>
            </div>
            """, unsafe_allow_html=True)
        with c_b:
            st.markdown("""
            <div class="stCard3D">
                <h4>Autonomous Diagnostic Warnings</h4>
                <p style="font-size:13px;color:#ff5c6c;">🔴 Class Imbalance: 'Missing Cap' is underrepresented by 52%.</p>
                <p style="font-size:13px;color:#eebd4c;">🟡 Data Leakage: 12 duplicate image hashes detected.</p>
                <p style="font-size:13px;color:#6477ff;">🔵 Quality Issue: 8% frames exhibit motion blur.</p>
            </div>
            """, unsafe_allow_html=True)

    with ai_col:
        st.markdown("""
        <div class="stCard3D">
            <h3 style="color:#6477ff;">✦ AI Copilot</h3>
            <p style="font-size:13px;color:#dbe4f8;background:rgba(18,32,57,0.8);padding:12px;border-radius:10px;">
                Detected class imbalance. Should I apply synthetic diffusion sampling to fix it?
            </p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Fix Data Imbalance", key="btn_fix_bal", use_container_width=True):
            st.toast("Generating synthetic missing cap images...")
        if st.button("Deduplicate Dataset", key="btn_dedup", use_container_width=True):
            st.toast("Removed 12 duplicate frames.")

def render_dataset_audit():
    st.markdown("# ▤ Autonomous Dataset Health Audit")
    st.caption("Automatically find imbalance, data leakage, duplicate images, and low-quality annotations.")

    d1, d2, d3 = st.columns(3)
    with d1:
        st.markdown("""
        <div class="stCard3D">
            <h4>Imbalance Analyzer</h4>
            <p style="font-size:24px;color:#ff5c6c;font-weight:700;">Severe Imbalance</p>
            <p style="font-size:12px;color:#8390a7;">Required Ratio: 1:1:1<br>Current Ratio: 4.7 : 1.4 : 1.0</p>
        </div>
        """, unsafe_allow_html=True)
    with d2:
        st.markdown("""
        <div class="stCard3D">
            <h4>Quality Inspector</h4>
            <p style="font-size:24px;color:#eebd4c;font-weight:700;">388 Bad Frames</p>
            <p style="font-size:12px;color:#8390a7;">Blurry: 120 | Low Contrast: 180<br>Corrupted Labels: 88</p>
        </div>
        """, unsafe_allow_html=True)
    with d3:
        st.markdown("""
        <div class="stCard3D">
            <h4>Data Leakage Guard</h4>
            <p style="font-size:24px;color:#20d69a;font-weight:700;">12 Duplicates</p>
            <p style="font-size:12px;color:#8390a7;">Found duplicate frames in Train & Validation sets.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### Targeted Auto-Fixes")
    c1, c2 = st.columns(2)
    with c1:
        st.checkbox("Apply Class Augmentation (+1,500 'Missing Cap' frames)", key="chk1")
        st.checkbox("Filter Blurry Frames (Variance threshold < 100)", key="chk2")
    with c2:
        st.checkbox("Remove Duplicate Hashes from Validation Split", key="chk3")
        st.checkbox("Auto-Fix Out-of-Bounds Bounding Boxes", key="chk4")

    if st.button("✦ Execute Dataset Health Optimization", key="btn_run_audit"):
        st.success("Dataset health score improved from 84% to 98%!")

def render_automl():
    st.markdown("# ▣ Autonomous Model Architect Engine")
    st.caption("Select your target deployment hardware to auto-select and train optimal vision architectures.")

    target = st.selectbox(
        "Select Target Deployment Scenario",
        ["Factory Edge (Jetson Nano / Raspberry Pi)", "Cloud Server API (High Accuracy)", "Mobile Web (Real-time Latency)"],
        key="sb_target"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="stCard3D">
            <h3>Active Training Telemetry</h3>
            <p style="color:#6477ff;">Model: YOLOv8 Small (Auto-Selected)</p>
        </div>
        """, unsafe_allow_html=True)
        st.progress(68)
        st.caption("Epoch 12 / 50 — Loss: 0.024 | mAP@0.5: 0.872")

    with col2:
        st.markdown("""
        <div class="stCard3D">
            <h3>Benchmarked Architectures</h3>
        </div>
        """, unsafe_allow_html=True)
        df_models = pd.DataFrame({
            "Architecture": ["YOLOv8s (Selected)", "YOLOv8n", "YOLOv5s", "RT-DETR-ResNet"],
            "mAP@0.5": [0.872, 0.843, 0.821, 0.798],
            "FPS (Jetson)": [142, 210, 165, 85],
            "Params (M)": [11.2, 3.2, 7.2, 32.0]
        })
        st.dataframe(df_models, hide_index=True, use_container_width=True)

def render_inspector():
    st.markdown("# 🧪 Real-World Reliability Inspector")
    st.caption("Stress-test vision models against edge environment conditions before deployment.")

    st.subheader("Simulate Factory Environmental Conditions")
    col1, col2 = st.columns(2)
    
    with col1:
        lighting = st.slider("Lighting Brightness Reduction (%)", 0, 80, 20, key="sld_light")
        blur_val = st.slider("Camera Motion Blur Simulation", 0, 10, 2, key="sld_blur")
    with col2:
        occlusion = st.slider("Object Occlusion (%)", 0, 50, 10, key="sld_occ")
        noise = st.slider("Sensor Noise (ISO Grain)", 0, 100, 15, key="sld_noise")

    st.markdown("<br>", unsafe_allow_html=True)
    reliability_score = max(30, 95 - (lighting*0.3 + blur_val*3 + occlusion*0.8 + noise*0.2))
    
    st.markdown(f"""
    <div class="stCard3D">
        <h3>Estimated Real-World Reliability Confidence</h3>
        <h1 style="color:{'#20d69a' if reliability_score > 75 else '#ff5c6c'};">{reliability_score:.1f}% Expected Accuracy</h1>
        <p style="color:#8390a7;">Diagnostic: Model is sensitive to high occlusion and dark conditions. Collect side-view dark samples to patch this gap.</p>
    </div>
    """, unsafe_allow_html=True)

def render_deployment():
    st.markdown("# ◉ Edge Deployment & Drift Monitoring")
    st.caption("Continuous endpoint telemetry, concept drift detection, and auto-retraining triggers.")

    m1, m2, m3 = st.columns(3)
    m1.metric("Endpoint Status", "Active (Edge)", "Latency: 12ms")
    m2.metric("Data Drift Index", "0.14", "Normal Bounds")
    m3.metric("Auto-Retrain Status", "Standby", "Triggers at Drift > 0.30")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Production Inference Telemetry Stream")
    
    chart_data = pd.DataFrame(
        np.random.randn(20, 2) / [50, 50] + [0.87, 0.05],
        columns=['Accuracy Score', 'Drift Metric']
    )
    st.line_chart(chart_data)

    if st.button("⚡ Trigger Emergency Auto-Retrain Pipeline", key="btn_retrain"):
        st.info("Auto-Retraining pipeline dispatched to GPU cluster.")


# ---------------------------------------------------------
# 3. MAIN ROUTER
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("### ✦ <span style='color:#6477ff;font-weight:800;font-size:22px;'>VisionForge AI</span>", unsafe_allow_html=True)
    st.markdown("---")
    
    selected_page = st.radio(
        "Modules",
        [
            "⌂ Home Dashboard",
            "▤ Dataset Health Audit",
            "▣ AutoML Training",
            "🧪 Real-World Inspector",
            "◉ Deployment & Drift"
        ],
        key="nav_radio"
    )
    
    st.markdown("---")
    st.caption("Active Pipeline")
    st.markdown("**Bottle Defect Detection**")
    st.progress(68)
    st.caption("Phase: Model Training (68%)")

# Page Routing Execution
if selected_page == "⌂ Home Dashboard":
    render_dashboard()
elif selected_page == "▤ Dataset Health Audit":
    render_dataset_audit()
elif selected_page == "▣ AutoML Training":
    render_automl()
elif selected_page == "🧪 Real-World Inspector":
    render_inspector()
elif selected_page == "◉ Deployment & Drift":
    render_deployment()
