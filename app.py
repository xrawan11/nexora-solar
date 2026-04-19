import streamlit as st
import base64

st.set_page_config(page_title="Nexora Solar", layout="wide")

# ضع صورة الخلفية باسم bg.jpg في نفس ملفات كولاب
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg = get_base64("bg.jpg")

st.markdown(f"""
<style>
html, body, [class*="css"] {{
    margin:0;
    padding:0;
    color:white;
    font-family:Arial, sans-serif;
}}

header, #MainMenu, footer {{
    visibility:hidden;
}}

.block-container {{
    padding:0;
    max-width:100%;
}}

.stApp {{
background:
linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.75)),
url("data:image/jpeg;base64,{bg}");
background-size:cover;
background-position:center;
background-attachment:fixed;
}}

.topbar {{
display:flex;
justify-content:space-between;
align-items:center;
padding:28px 40px;
}}

.logo {{
font-size:42px;
font-weight:900;
color:#f6b73c;
letter-spacing:2px;
}}

.menu {{
font-size:38px;
font-weight:bold;
}}

.hero {{
text-align:center;
padding-top:70px;
}}

.hero h1 {{
font-size:82px;
font-weight:900;
line-height:1.05;
margin-bottom:25px;
}}

.gold {{
color:#f6b73c;
}}

.btn {{
display:inline-block;
margin-top:20px;
background:#f6b73c;
color:black;
padding:18px 42px;
border-radius:16px;
font-size:24px;
font-weight:900;
}}

.grid {{
padding:80px 70px 40px 70px;
}}

.card {{
background:rgba(0,0,0,0.45);
border:1px solid rgba(255,255,255,0.08);
backdrop-filter:blur(10px);
border-radius:22px;
padding:28px;
text-align:center;
box-shadow:0 0 25px rgba(246,183,60,0.12);
}}

.card h2 {{
font-size:56px;
margin:0;
color:#f6b73c;
font-weight:900;
}}

.card p {{
font-size:20px;
margin-top:8px;
color:#d9d9d9;
}}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="topbar">
<div class="logo">☀ NEXORA</div>
<div class="menu">☰</div>
</div>

<div class="hero">
<h1>
Where Energy Is <br>
<span class="gold">Managed, Not Wasted</span>
</h1>

<div class="btn">Let's Start Today →</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="grid">', unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown('<div class="card"><h2>15K+</h2><p>Installations</p></div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card"><h2>98+</h2><p>Projects Completed</p></div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="card"><h2>40%</h2><p>Avg. Cost Saving</p></div>', unsafe_allow_html=True)

with c4:
    st.markdown('<div class="card"><h2>12</h2><p>Years Experience</p></div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
