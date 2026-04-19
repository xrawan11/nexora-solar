import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Nexora Solar", page_icon="☀️", layout="wide")

# ---------------- STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "report_type" not in st.session_state:
    st.session_state.report_type = "Daily"

def go(page):
    st.session_state.page = page
    st.rerun()

# ---------------- STYLE ----------------
st.markdown("""
<style>
html, body, [class*="css"]{
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
font-size:36px;
font-weight:900;
font-style:italic;
letter-spacing:2px;
color:white;
}
.sun{
color:#f6b73c;
text-shadow:
0 0 6px rgba(246,183,60,.8),
0 0 12px rgba(246,183,60,.55),
0 0 18px rgba(246,183,60,.3);
}

/* splash */
.splash{
height:90vh;
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
0%{opacity:0;transform:scale(.75);}
40%{opacity:1;transform:scale(1);}
70%{opacity:1;}
100%{opacity:0;transform:scale(1.05);}
}

/* hero */
.hero{
text-align:center;
padding:45px 0 35px 0;
}
.hero h1{
font-size:72px;
font-weight:900;
line-height:1.08;
margin-bottom:18px;
}
.gold{
color:#f6b73c;
animation:goldpulse 2s infinite;
}
@keyframes goldpulse{
50%{
text-shadow:0 0 18px rgba(246,183,60,.45);
}
}
.desc{
max-width:950px;
margin:auto;
font-size:20px;
line-height:1.7;
color:#d5d5d5;
}

/* stats */
.stat{
background:#101010;
border:1px solid #222;
border-radius:18px;
padding:22px;
height:150px;
text-align:center;
}
.stat h2{
margin:0;
font-size:42px;
color:#f6b73c;
}

/* main cards */
.main{
background:#101010;
border:1px solid #222;
border-radius:22px;
padding:24px;
min-height:430px;
transition:.25s;
cursor:pointer;
box-shadow:0 0 10px rgba(246,183,60,.05);
}
.main:hover{
transform:translateY(-8px);
border-color:#f6b73c;
box-shadow:
0 0 10px rgba(246,183,60,.12),
0 0 24px rgba(246,183,60,.10),
0 0 40px rgba(246,183,60,.06);
}
.main-title{
font-size:30px;
font-weight:900;
color:#f6b73c;
margin-bottom:18px;
}
.subitem{
padding:12px 14px;
margin-bottom:10px;
border-radius:12px;
background:#151515;
border:1px solid #222;
font-size:17px;
font-weight:700;
color:white;
}

/* section pages */
.title{
font-size:48px;
font-weight:900;
color:#f6b73c;
margin:10px 0 20px 0;
}
.subtitle{
font-size:30px;
font-weight:800;
margin:25px 0 10px 0;
}
.reportbox{
background:#111;
border:1px solid #222;
border-radius:18px;
padding:20px;
margin-top:12px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- INTRO ----------------
holder = st.empty()
holder.markdown("""
<div class="splash">
NEX<span class="sun">O</span>RA
</div>
""", unsafe_allow_html=True)
time.sleep(2)
holder.empty()

# ---------------- TOP ----------------
a,b = st.columns([8,1])

with a:
    st.markdown('<div class="logo">NEX<span class="sun">O</span>RA</div>', unsafe_allow_html=True)

with b:
    with st.popover("☰"):
        if st.button("Home"): go("home")
        if st.button("Performance"): go("performance")
        if st.button("Expected Data"): go("expected")
        if st.button("Battery Status"): go("battery")

# ---------------- BACK ----------------
if st.session_state.page != "home":
    c1,c2 = st.columns([8,1])
    with c2:
        if st.button("← Back"):
            go("home")

# ---------------- HOME ----------------
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

    if st.button("Let's Start Today →"):
        go("performance")

    s1,s2,s3,s4 = st.columns(4)
    vals=[("15K+","Installations"),("98+","Projects"),("40%","Saving"),("12","Years")]
    for col,(n,t) in zip([s1,s2,s3,s4],vals):
        with col:
            st.markdown(f'<div class="stat"><h2>{n}</h2><p>{t}</p></div>', unsafe_allow_html=True)

    st.write("")

    c1,c2,c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="main">
        <div class="main-title">Performance</div>
        <div class="subitem">Current Performance</div>
        <div class="subitem">Profits / Losses</div>
        <div class="subitem">Comparison</div>
        <div class="subitem">Reports</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Performance", key="p_home"):
            go("performance")

    with c2:
        st.markdown("""
        <div class="main">
        <div class="main-title">Expected Data</div>
        <div class="subitem">Weather</div>
        <div class="subitem">Predictive Maintenance</div>
        <div class="subitem">Expected Energy Production</div>
        <div class="subitem">Best Time for Operation</div>
        <div class="subitem">Recommendations + Alerts</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Expected", key="e_home"):
            go("expected")

    with c3:
        st.markdown("""
        <div class="main">
        <div class="main-title">Battery Status</div>
        <div class="subitem">Energy Inventory</div>
        <div class="subitem">Electrical Metrics</div>
        <div class="subitem">Battery Health</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Battery", key="b_home"):
            go("battery")

# ---------------- PERFORMANCE ----------------
elif st.session_state.page == "performance":

    st.markdown('<div class="title">Performance</div>', unsafe_allow_html=True)

    st.markdown('<div class="subtitle">Current Performance</div>', unsafe_allow_html=True)
    a,b,c = st.columns(3)
    a.metric("Current Energy","520 kW")
    b.metric("Production","1800 kWh")
    c.metric("Efficiency","94%")

    st.markdown('<div class="subtitle">Profits / Losses</div>', unsafe_allow_html=True)
    a,b,c = st.columns(3)
    a.metric("Revenue","$12,400")
    b.metric("Profits","$8,100")
    c.metric("Losses","$1,240")

    st.markdown('<div class="subtitle">Comparison</div>', unsafe_allow_html=True)
    st.write("Actual vs Expected")
    st.line_chart({"Actual":[420,510,490],"Expected":[450,520,505]})

    st.markdown('<div class="subtitle">Reports</div>', unsafe_allow_html=True)

    r1,r2,r3 = st.columns(3)
    with r1:
        if st.button("Daily"):
            st.session_state.report_type="Daily"
    with r2:
        if st.button("Weekly"):
            st.session_state.report_type="Weekly"
    with r3:
        if st.button("Monthly"):
            st.session_state.report_type="Monthly"

    st.markdown(f"""
    <div class="reportbox">
    <b>{st.session_state.report_type} Report Preview</b><br><br>
    Output Stable<br>
    Efficiency Good<br>
    Revenue Positive
    </div>
    """, unsafe_allow_html=True)

    st.download_button("PDF", data="Report", file_name="report.pdf")

# ---------------- EXPECTED ----------------
elif st.session_state.page == "expected":

    st.markdown('<div class="title">Expected Data</div>', unsafe_allow_html=True)

    st.markdown('<div class="subtitle">Weather</div>', unsafe_allow_html=True)
    st.line_chart({"Day1":[34],"Day2":[35],"Day3":[33],"Day4":[36]})

    st.markdown('<div class="subtitle">Predictive Maintenance</div>', unsafe_allow_html=True)
    a,b = st.columns(2)
    a.metric("Clean","78%")
    b.metric("Dusty","22%")

    st.markdown('<div class="subtitle">Expected Energy Production</div>', unsafe_allow_html=True)
    st.write("Predicted Output: 2100 kWh")

    st.markdown('<div class="subtitle">Best Time for Operation</div>', unsafe_allow_html=True)
    st.success("11 AM - 2 PM")

    st.markdown('<div class="subtitle">Recommendations + Alerts</div>', unsafe_allow_html=True)
    st.warning("Clean panels this week.")

# ---------------- BATTERY ----------------
elif st.session_state.page == "battery":

    st.markdown('<div class="title">Battery Status</div>', unsafe_allow_html=True)

    st.markdown('<div class="subtitle">Energy Inventory</div>', unsafe_allow_html=True)
    st.metric("Stored Energy","82%")

    st.markdown('<div class="subtitle">Electrical Metrics</div>', unsafe_allow_html=True)
    a,b,c = st.columns(3)
    a.metric("Voltage","412 V")
    b.metric("Current","32 A")
    c.metric("Temp","31°C")

    st.markdown('<div class="subtitle">Battery Health</div>', unsafe_allow_html=True)
    st.metric("Life Span","8.4 Years")
