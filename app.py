import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Nexora Solar", page_icon="☀️", layout="wide")

# ---------------- STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "section" not in st.session_state:
    st.session_state.section = ""

if "report_type" not in st.session_state:
    st.session_state.report_type = "Daily"

def go(page, section=""):
    st.session_state.page = page
    st.session_state.section = section
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

.logo{
font-size:36px;
font-weight:900;
font-style:italic;
color:white;
letter-spacing:2px;
}
.sun{
color:#f6b73c;
text-shadow:0 0 6px rgba(246,183,60,.8),
0 0 12px rgba(246,183,60,.55),
0 0 18px rgba(246,183,60,.3);
}

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
40%{opacity:1;}
70%{opacity:1;}
100%{opacity:0;transform:scale(1.05);}
}

.hero{text-align:center;padding:45px 0 35px 0;}
.hero h1{
font-size:72px;
font-weight:900;
line-height:1.08;
}
.gold{
color:#f6b73c;
animation:glow 2s infinite;
}
@keyframes glow{
50%{text-shadow:0 0 18px rgba(246,183,60,.45);}
}
.desc{
max-width:950px;
margin:auto;
font-size:20px;
line-height:1.7;
color:#d5d5d5;
}

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

.main{
background:#101010;
border:1px solid #222;
border-radius:22px;
padding:24px;
min-height:420px;
transition:.25s;
box-shadow:0 0 12px rgba(246,183,60,.08);
}
.main:hover{
transform:translateY(-8px);
border-color:#f6b73c;
box-shadow:0 0 24px rgba(246,183,60,.14);
}

.main-title{
font-size:30px;
font-weight:900;
color:#f6b73c;
margin-bottom:16px;
}

.title{
font-size:48px;
font-weight:900;
color:#f6b73c;
margin:10px 0 20px 0;
}

.subtitle{
font-size:30px;
font-weight:800;
margin:28px 0 10px 0;
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
        if st.button("Battery"): go("battery")

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
    <h1>Where Energy Is <span class="gold">Managed</span><br>Not Wasted</h1>
    <div class="desc">
    Energy is intelligently captured, monitored, and optimized for real-world use.
    This space aims to improve workflow quality, reduce company workload,
    and enable efficient and flexible operations.
    </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Let's Start Today →"):
        go("performance", "current")

    s1,s2,s3,s4 = st.columns(4)
    vals=[("15K+","Installations"),("98+","Projects"),("40%","Saving"),("12","Years")]
    for col,(n,t) in zip([s1,s2,s3,s4],vals):
        with col:
            st.markdown(f'<div class="stat"><h2>{n}</h2><p>{t}</p></div>', unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.write("")

    c1,c2,c3 = st.columns(3)

    with c1:
        st.markdown('<div class="main"><div class="main-title">Performance</div></div>', unsafe_allow_html=True)
        if st.button("Current Performance", key="p1"): go("performance","current")
        if st.button("Profits / Losses", key="p2"): go("performance","profits")
        if st.button("Comparison", key="p3"): go("performance","compare")
        if st.button("Reports", key="p4"): go("performance","reports")

    with c2:
        st.markdown('<div class="main"><div class="main-title">Expected Data</div></div>', unsafe_allow_html=True)
        if st.button("Weather", key="e1"): go("expected","weather")
        if st.button("Predictive Maintenance", key="e2"): go("expected","maint")
        if st.button("Expected Energy Production", key="e3"): go("expected","energy")
        if st.button("Best Time for Operation", key="e4"): go("expected","best")
        if st.button("Recommendations + Alerts", key="e5"): go("expected","alerts")

    with c3:
        st.markdown('<div class="main"><div class="main-title">Battery Status</div></div>', unsafe_allow_html=True)
        if st.button("Energy Inventory", key="b1"): go("battery","inventory")
        if st.button("Electrical Metrics", key="b2"): go("battery","metrics")
        if st.button("Battery Health", key="b3"): go("battery","health")

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
    st.bar_chart([4,6,8,7,10,12])

    st.markdown('<div class="subtitle">Comparison</div>', unsafe_allow_html=True)
    st.write("Actual vs Expected")
    st.line_chart({"Actual":[420,510,490],"Expected":[450,520,505]})
    st.write("Today vs Yesterday")
    st.line_chart({"Today":[410,520,500],"Yesterday":[390,500,480]})
    st.write("This Month vs Last Month")
    st.bar_chart({"This":[12],"Last":[10]})
    st.write("Our System vs Ideal System")
    st.bar_chart({"Our":[94],"Ideal":[100]})

    st.markdown('<div class="subtitle">Reports</div>', unsafe_allow_html=True)

    r1,r2,r3 = st.columns(3)
    with r1:
        if st.button("Daily"): st.session_state.report_type="Daily"
    with r2:
        if st.button("Weekly"): st.session_state.report_type="Weekly"
    with r3:
        if st.button("Monthly"): st.session_state.report_type="Monthly"

    st.info(f"{st.session_state.report_type} Report Preview")
    st.download_button("PDF Download","Report",file_name="report.pdf")

# ---------------- EXPECTED ----------------
elif st.session_state.page == "expected":

    st.markdown('<div class="title">Expected Data</div>', unsafe_allow_html=True)

    st.markdown('<div class="subtitle">Weather</div>', unsafe_allow_html=True)
    a,b,c,d,e = st.columns(5)
    a.metric("Temp","34°C")
    b.metric("Humidity","48%")
    c.metric("Cloud","15%")
    d.metric("Wind","9 km/h")
    e.metric("Irradiation","920 W/m²")
    st.line_chart({"Day1":[34],"Day2":[35],"Day3":[33],"Day4":[36]})

    st.markdown('<div class="subtitle">Predictive Maintenance</div>', unsafe_allow_html=True)
    st.file_uploader("Upload Image")
    a,b = st.columns(2)
    a.metric("Clean","78%")
    b.metric("Dusty","22%")
    st.info("Cleaning recommended soon.")

    st.markdown('<div class="subtitle">Expected Energy Production</div>', unsafe_allow_html=True)
    st.write("Predicted Output: 2100 kWh")
    st.write("Factors: Weather / Battery / Clean Panels / Low Shading")

    st.markdown('<div class="subtitle">Best Time for Operation</div>', unsafe_allow_html=True)
    st.success("11 AM - 2 PM")

    st.markdown('<div class="subtitle">Recommendations + Alerts</div>', unsafe_allow_html=True)
    st.warning("Clean panels this week.")
    st.success("Run heavy loads at noon.")

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
    st.line_chart([95,92,90,88,85,82])
