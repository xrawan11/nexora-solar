import streamlit as st

st.set_page_config(
    page_title="Nexora Solar",
    page_icon="☀️",
    layout="wide"
)

st.markdown("""
<style>
html, body, [class*="css"]{
background: linear-gradient(135deg,#050505,#111111,#1a1200);
color:white;
}

header,#MainMenu,footer{
visibility:hidden;
}

.block-container{
padding-top:1rem;
padding-left:2rem;
padding-right:2rem;
}

.logo{
font-size:38px;
font-weight:900;
color:#f6b73c;
}

.nav{
text-align:right;
font-size:18px;
color:#ddd;
}

.hero{
text-align:center;
padding-top:90px;
padding-bottom:55px;
}

.hero h1{
font-size:76px;
font-weight:900;
line-height:1.1;
}

.gold{
color:#f6b73c;
}

.btn{
display:inline-block;
background:#f6b73c;
color:black;
padding:16px 38px;
border-radius:14px;
font-size:22px;
font-weight:800;
margin-top:24px;
}

.card{
background:rgba(255,255,255,0.03);
border:1px solid rgba(255,255,255,0.08);
border-radius:18px;
padding:25px;
text-align:center;
}

.card h2{
font-size:46px;
margin:0;
color:#f6b73c;
}

.card p{
font-size:18px;
color:#cfcfcf;
margin-top:8px;
}
</style>
""", unsafe_allow_html=True)

a,b = st.columns([6,4])

with a:
    st.markdown('<div class="logo">☀ NEXORA</div>', unsafe_allow_html=True)

with b:
    st.markdown('<div class="nav">Home &nbsp;&nbsp; Performance &nbsp;&nbsp; Battery &nbsp;&nbsp; Reports</div>', unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>
Where Energy Is <br>
<span class="gold">Managed, Not Wasted</span>
</h1>

<div class="btn">Let's Start Today →</div>
</div>
""", unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown('<div class="card"><h2>15K+</h2><p>Installations</p></div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card"><h2>98+</h2><p>Projects Completed</p></div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="card"><h2>40%</h2><p>Avg. Cost Saving</p></div>', unsafe_allow_html=True)

with c4:
    st.markdown('<div class="card"><h2>12</h2><p>Years Experience</p></div>', unsafe_allow_html=True)
