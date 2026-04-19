import streamlit as st

st.set_page_config(page_title="Nexora Solar", layout="wide")

st.markdown("""
<style>
html,body,[class*="css"]{background:#050505;color:white;font-family:Arial;}
header,#MainMenu,footer{visibility:hidden;}
.block-container{padding:0 2rem;max-width:1450px;}

.logo{
font-size:42px;
font-weight:900;
font-style:italic;
color:white;
letter-spacing:2px;
}
.sun{
color:#f6b73c;
text-shadow:0 0 15px rgba(246,183,60,.6);
}

.hero{text-align:center;padding-top:70px;padding-bottom:30px;}
.hero h1{font-size:78px;font-weight:900;line-height:1.05;}
.gold{color:#f6b73c;}

.desc{
max-width:950px;
margin:auto;
font-size:20px;
line-height:1.7;
color:#d5d5d5;
}

.btn{
display:inline-block;
margin-top:28px;
padding:16px 38px;
border-radius:14px;
background:#f6b73c;
color:black;
font-size:22px;
font-weight:900;
animation:pulse 2s infinite;
}
@keyframes pulse{
50%{box-shadow:0 0 20px rgba(246,183,60,.45);}
}

.stat{
background:#111;
border:1px solid #222;
border-radius:18px;
padding:28px;
height:155px;
text-align:center;
}
.stat h2{margin:0;color:#f6b73c;font-size:42px;}
.stat p{margin-top:10px;color:#ccc;}

.main{
background:#0d0d0d;
border:1px solid #202020;
border-radius:22px;
padding:26px;
height:100%;
transition:.25s;
}
.main:hover{
transform:translateY(-8px);
border-color:#f6b73c;
box-shadow:0 0 20px rgba(246,183,60,.15);
}
.main h3{
font-size:28px;
color:#f6b73c;
margin-bottom:18px;
}

.opt{
padding:12px 14px;
border-radius:12px;
background:#151515;
margin-bottom:10px;
border:1px solid #222;
}
.opt:hover{
border-color:#f6b73c;
background:#1b1b1b;
}

.section{
font-size:48px;
font-weight:900;
margin-top:80px;
margin-bottom:20px;
color:#f6b73c;
}

.sub{
font-size:28px;
font-weight:800;
margin-top:28px;
margin-bottom:10px;
}

.box{
background:#101010;
border:1px solid #222;
border-radius:18px;
padding:22px;
margin-bottom:16px;
}
</style>
""", unsafe_allow_html=True)

# top
a,b=st.columns([8,1])
with a:
    st.markdown('<div class="logo">NEX<span class="sun">O</span>RA</div>', unsafe_allow_html=True)
with b:
    st.markdown('<div style="font-size:34px;text-align:right;">☰</div>', unsafe_allow_html=True)

# hero
st.markdown("""
<div class="hero">
<h1>Where Energy Is <span class="gold">Managed</span><br>Not Wasted</h1>
<div class="desc">
Energy is intelligently captured, monitored, and optimized for real-world use.
This space aims to improve workflow quality, reduce company workload, and enable efficient and flexible operations.
</div>
<div class="btn">Let's Start Today →</div>
</div>
""", unsafe_allow_html=True)

# stats
c1,c2,c3,c4=st.columns(4)
items=[("15K+","Installations"),("98+","Projects Completed"),("40%","Avg. Cost Saving"),("12","Years Experience")]
for col,(n,t) in zip([c1,c2,c3,c4],items):
    with col:
        st.markdown(f'<div class="stat"><h2>{n}</h2><p>{t}</p></div>', unsafe_allow_html=True)

# main sections
st.markdown('<div class="section">Core Sections</div>', unsafe_allow_html=True)

x1,x2,x3=st.columns(3)

with x1:
    st.markdown("""
<div class="main">
<h3>Performance</h3>
<div class="opt">Current Performance</div>
<div class="opt">Profits / Losses</div>
<div class="opt">Reports</div>
<div class="opt">Comparison</div>
</div>
""", unsafe_allow_html=True)

with x2:
    st.markdown("""
<div class="main">
<h3>Expected Data</h3>
<div class="opt">Weather</div>
<div class="opt">Predictive Maintenance</div>
<div class="opt">Expected Energy Production</div>
<div class="opt">Best Time for Operation</div>
<div class="opt">Recommendations + Alerts</div>
</div>
""", unsafe_allow_html=True)

with x3:
    st.markdown("""
<div class="main">
<h3>Battery Status</h3>
<div class="opt">Energy Inventory</div>
<div class="opt">Electrical Metrics</div>
<div class="opt">Battery Status</div>
</div>
""", unsafe_allow_html=True)
