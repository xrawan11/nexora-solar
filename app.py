import streamlit as st

st.set_page_config(
    page_title="Nexora Solar",
    page_icon="☀️",
    layout="wide"
)

st.markdown("""
<style>
html, body, [class*="css"]{
background: linear-gradient(135deg,#030303,#0b0b0b,#1a1200);
color:white;
font-family:Arial, sans-serif;
}

header,#MainMenu,footer{
visibility:hidden;
}

.block-container{
padding-top:1rem;
padding-left:2rem;
padding-right:2rem;
max-width:1400px;
}

.logo{
font-size:40px;
font-weight:900;
color:#f6b73c;
letter-spacing:2px;
}

.nav{
text-align:right;
font-size:17px;
color:#d7d7d7;
padding-top:10px;
}

.hero{
text-align:center;
padding-top:70px;
padding-bottom:45px;
}

.hero h1{
font-size:72px;
font-weight:900;
line-height:1.08;
margin-bottom:18px;
}

.gold{
color:#f6b73c;
}

.sub{
font-size:22px;
color:#bfbfbf;
margin-bottom:25px;
}

.btn{
display:inline-block;
background:#f6b73c;
color:black;
padding:16px 38px;
border-radius:14px;
font-size:22px;
font-weight:800;
margin-top:10px;
}

.stat{
background:rgba(255,255,255,0.03);
border:1px solid rgba(255,255,255,0.08);
border-radius:18px;
padding:22px;
text-align:center;
margin-top:8px;
}

.stat h2{
font-size:42px;
margin:0;
color:#f6b73c;
}

.stat p{
font-size:16px;
color:#d4d4d4;
margin-top:8px;
}

.section-title{
font-size:40px;
font-weight:900;
margin-top:60px;
margin-bottom:25px;
}

.card{
background:rgba(255,255,255,0.035);
border:1px solid rgba(255,255,255,0.07);
border-radius:20px;
padding:24px;
height:100%;
}

.card h3{
font-size:28px;
margin-bottom:12px;
color:#f6b73c;
}

.tag{
display:inline-block;
padding:7px 12px;
border-radius:999px;
background:rgba(246,183,60,0.12);
border:1px solid rgba(246,183,60,0.25);
font-size:13px;
margin:4px;
color:#ffd98a;
}

.small{
color:#bcbcbc;
line-height:1.7;
font-size:16px;
}
</style>
""", unsafe_allow_html=True)

# Top bar
a,b = st.columns([5,5])
with a:
    st.markdown('<div class="logo">☀ NEXORA</div>', unsafe_allow_html=True)
with b:
    st.markdown('<div class="nav">Home &nbsp;&nbsp; Dashboard &nbsp;&nbsp; AI Insights &nbsp;&nbsp; Contact</div>', unsafe_allow_html=True)

# Hero
st.markdown("""
<div class="hero">
<h1>
Where Energy Is <br>
<span class="gold">Managed, Not Wasted</span>
</h1>
<div class="sub">Premium solar intelligence platform for monitoring, prediction, and battery control.</div>
<div class="btn">Let's Start Today →</div>
</div>
""", unsafe_allow_html=True)

# Stats
s1,s2,s3,s4 = st.columns(4)
stats = [
("15K+","Installations"),
("98+","Projects Completed"),
("40%","Avg. Cost Saving"),
("12","Years Experience")
]
for col,(num,txt) in zip([s1,s2,s3,s4],stats):
    with col:
        st.markdown(f'<div class="stat"><h2>{num}</h2><p>{txt}</p></div>', unsafe_allow_html=True)

# Main Sections
st.markdown('<div class="section-title">Core Platform Sections</div>', unsafe_allow_html=True)

c1,c2,c3 = st.columns(3)

with c1:
    st.markdown("""
<div class="card">
<h3>⚡ Performance</h3>
<div class="small">Track real-time generation, ROI, and operational efficiency.</div><br>
<span class="tag">Current Performance</span>
<span class="tag">Profits / Losses</span>
<span class="tag">Reports</span>
<span class="tag">Comparison</span>
</div>
""", unsafe_allow_html=True)

with c2:
    st.markdown("""
<div class="card">
<h3>☁ Expected Data</h3>
<div class="small">Use forecasting models and AI recommendations to maximize production.</div><br>
<span class="tag">Weather</span>
<span class="tag">Predictive Maintenance</span>
<span class="tag">Energy Forecast</span>
<span class="tag">Alerts</span>
</div>
""", unsafe_allow_html=True)

with c3:
    st.markdown("""
<div class="card">
<h3>🔋 Battery System</h3>
<div class="small">Monitor storage assets, health metrics, and charging strategy.</div><br>
<span class="tag">Energy Inventory</span>
<span class="tag">Voltage / Temp</span>
<span class="tag">Battery Status</span>
<span class="tag">Lifecycle</span>
</div>
""", unsafe_allow_html=True)

# Footer note
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("Nexora Solar Intelligence Platform © 2026")
