import streamlit as st
import pandas as pd
import time

st.set_page_config(
    page_title="Nexora Solar",
    page_icon="☀️",
    layout="wide"
)

# ---------------- STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

def go(x):
    st.session_state.page = x
    st.rerun()

# ---------------- STYLE ----------------
st.markdown("""
<style>
html,body,[class*="css"]{
background:#050505;
color:white;
font-family:Arial,sans-serif;
}
header,#MainMenu,footer{visibility:hidden;}
.block-container{
max-width:1450px;
padding-top:1rem;
padding-left:2rem;
padding-right:2rem;
}

/* logo */
.logo{
font-size:34px;
font-weight:900;
font-style:italic;
color:white;
letter-spacing:2px;
}
.sun{
color:#f6b73c;
text-shadow:
0 0 5px rgba(246,183,60,.8),
0 0 12px rgba(246,183,60,.45);
}

/* intro */
.splash{
height:88vh;
display:flex;
justify-content:center;
align-items:center;
font-size:64px;
font-weight:900;
font-style:italic;
opacity:0;
animation:intro 2s ease forwards;
}
@keyframes intro{
0%{opacity:0;transform:scale(.8);}
40%{opacity:1;}
70%{opacity:1;}
100%{opacity:0;transform:scale(1.05);}
}

/* hero */
.hero{
text-align:center;
padding:45px 0 25px 0;
}
.hero h1{
font-size:68px;
font-weight:900;
line-height:1.08;
}
.gold{
color:#f6b73c;
text-shadow:0 0 16px rgba(246,183,60,.25);
}
.desc{
max-width:950px;
margin:auto;
font-size:19px;
line-height:1.7;
color:#d4d4d4;
}

/* stats */
.stat{
background:#101010;
border:1px solid #222;
border-radius:16px;
padding:18px;
height:135px;
text-align:center;
}
.stat h2{
margin:0;
font-size:36px;
color:#f6b73c;
}

/* cards */
.main{
background:#101010;
border:1px solid #222;
border-radius:20px;
padding:18px;
min-height:220px;
transition:.18s;
box-shadow:0 0 10px rgba(246,183,60,.05);
cursor:pointer;
}
.main:hover{
transform:translateY(-6px);
border-color:#f6b73c;
box-shadow:0 0 18px rgba(246,183,60,.12);
}
.main-title{
font-size:28px;
font-weight:900;
color:#f6b73c;
margin-bottom:10px;
}

/* titles */
.title{
font-size:46px;
font-weight:900;
color:#f6b73c;
margin:8px 0 18px 0;
}
.subtitle{
font-size:28px;
font-weight:800;
margin:26px 0 10px 0;
}

/* buttons */
div.stButton > button{
width:100%;
border-radius:12px;
border:1px solid #333;
background:#111;
color:white;
transition:.15s;
}
div.stButton > button:hover{
border-color:#f6b73c;
color:#f6b73c;
}
</style>
""", unsafe_allow_html=True)

# ---------------- INTRO ----------------
intro = st.empty()
intro.markdown("""
<div class="splash">
NEX<span class="sun">O</span>RA
</div>
""", unsafe_allow_html=True)
time.sleep(2)
intro.empty()

# ---------------- TOP ----------------
a,b = st.columns([8,1])

with a:
    st.markdown('<div class="logo">NEX<span class="sun">O</span>RA</div>', unsafe_allow_html=True)

with b:
    with st.popover("☰"):
        if st.button("Home", key="n1"):
            go("home")
        if st.button("Performance", key="n2"):
            go("performance")
        if st.button("Expected Data", key="n3"):
            go("expected")
        if st.button("Battery Status", key="n4"):
            go("battery")

# ---------------- BACK ----------------
if st.session_state.page != "home":
    c1,c2 = st.columns([8,1])
    with c2:
        if st.button("← Back", key="bk"):
            go("home")

# =====================================================
# HOME
# =====================================================
if st.session_state.page == "home":

    st.markdown("""
    <div class="hero">
    <h1>
    Where Energy Is <span class="gold">Managed</span><br>
    Not Wasted
    </h1>
    <div class="desc">
    Energy is intelligently captured, monitored, and optimized for real-world use.
    This space aims to improve workflow quality, reduce company workload,
    and enable efficient and flexible operations.
    </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Let's Start Today →", key="start"):
        go("performance")

    # wider spacing stats
    s1,sp1,s2,sp2,s3,sp3,s4 = st.columns([1,0.18,1,0.18,1,0.18,1])

    with s1:
        st.markdown('<div class="stat"><h2>15K+</h2><p>Installations</p></div>', unsafe_allow_html=True)
    with s2:
        st.markdown('<div class="stat"><h2>98+</h2><p>Projects</p></div>', unsafe_allow_html=True)
    with s3:
        st.markdown('<div class="stat"><h2>40%</h2><p>Saving</p></div>', unsafe_allow_html=True)
    with s4:
        st.markdown('<div class="stat"><h2>12</h2><p>Years</p></div>', unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.write("")

    # wider spacing main cards
    c1,g1,c2,g2,c3 = st.columns([1,0.28,1,0.28,1])

    with c1:
        st.markdown("""
        <div class="main">
        <div class="main-title">Performance</div>
        <p>Monitoring, reports, profits, comparisons.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button(" ", key="card1"):
            go("performance")

    with c2:
        st.markdown("""
        <div class="main">
        <div class="main-title">Expected Data</div>
        <p>Weather, AI forecasts, maintenance insights.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("  ", key="card2"):
            go("expected")

    with c3:
        st.markdown("""
        <div class="main">
        <div class="main-title">Battery Status</div>
        <p>Inventory, health, voltage and cycles.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("   ", key="card3"):
            go("battery")

# =====================================================
# PERFORMANCE
# =====================================================
elif st.session_state.page == "performance":

    st.markdown('<div class="title">Performance</div>', unsafe_allow_html=True)

    st.markdown('<div class="subtitle">Current Performance</div>', unsafe_allow_html=True)

    a,b,c = st.columns(3)
    a.metric("Current Energy","520 kW")
    b.metric("Production","1800 kWh")
    c.metric("Efficiency","94%")

    st.write("Live Output Graph - Last 24 Hours")
    st.line_chart(pd.DataFrame({
        "kW":[220,250,270,290,310,340,370,410,450,500,530,550,
              560,540,520,500,470,430,390,350,320,290,260,230]
    }))

# =====================================================
# EXPECTED
# =====================================================
elif st.session_state.page == "expected":

    st.markdown('<div class="title">Expected Data</div>', unsafe_allow_html=True)

    st.markdown('<div class="subtitle">Weather</div>', unsafe_allow_html=True)

    a,b,c,d,e = st.columns(5)
    a.metric("Temperature","34°C")
    b.metric("Humidity","48%")
    c.metric("Cloud Cover","15%")
    d.metric("Irradiation","920 W/m²")
    e.metric("Wind Speed","9 km/h")

# =====================================================
# BATTERY
# =====================================================
elif st.session_state.page == "battery":

    st.markdown('<div class="title">Battery Status</div>', unsafe_allow_html=True)

    a,b,c = st.columns(3)
    a.metric("Voltage","412 V")
    b.metric("Current","32 A")
    c.metric("Temp","31°C")
