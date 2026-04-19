import streamlit as st
import time
import pandas as pd

st.set_page_config(page_title="Nexora Solar", page_icon="☀️", layout="wide")

# ---------------- STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

def go(x):
    st.session_state.page = x
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
.block-container{max-width:1450px;padding-top:1rem;padding-left:2rem;padding-right:2rem;}

.logo{
font-size:44px;
font-weight:900;
font-style:italic;
letter-spacing:2px;
color:white;
}
.sun{
color:#f6b73c;
text-shadow:0 0 16px rgba(246,183,60,.6);
}

.hero{text-align:center;padding:55px 0 35px 0;}
.hero h1{font-size:72px;font-weight:900;line-height:1.08;}
.gold{color:#f6b73c;}
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
padding:22px;
min-height:420px;
transition:.25s;
}
.main:hover{
transform:translateY(-8px);
border-color:#f6b73c;
box-shadow:0 0 18px rgba(246,183,60,.15);
}

.main-title{
font-size:28px;
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
margin:25px 0 10px 0;
}

.small{
font-size:17px;
color:#d5d5d5;
line-height:1.8;
}

.backbtn button{
background:#111 !important;
color:white !important;
border:1px solid #333 !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TOP ----------------
a,b = st.columns([8,1])
with a:
    st.markdown('<div class="logo">NEX<span class="sun">O</span>RA</div>', unsafe_allow_html=True)

with b:
    with st.popover("☰"):
        if st.button("Home", key="nav0"): go("home")
        if st.button("Performance", key="nav1"): go("performance")
        if st.button("Expected Data", key="nav2"): go("expected")
        if st.button("Battery Status", key="nav3"): go("battery")

# ---------------- BACK TOP ----------------
if st.session_state.page != "home":
    c1,c2 = st.columns([8,1])
    with c2:
        st.markdown('<div class="backbtn">', unsafe_allow_html=True)
        if st.button("← Back", key="back_top"):
            go("home")
        st.markdown('</div>', unsafe_allow_html=True)

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

    if st.button("Let's Start Today →", key="start"):
        go("performance")

    s1,s2,s3,s4 = st.columns(4)
    stats=[("15K+","Installations"),("98+","Projects"),("40%","Saving"),("12","Years")]
    for col,(n,t) in zip([s1,s2,s3,s4],stats):
        with col:
            st.markdown(f'<div class="stat"><h2>{n}</h2><p>{t}</p></div>', unsafe_allow_html=True)

    st.write("")
    c1,c2,c3 = st.columns(3)

    with c1:
        st.markdown('<div class="main"><div class="main-title">Performance</div></div>', unsafe_allow_html=True)
        if st.button("Current Performance", key="h1"): go("performance")
        if st.button("Profits / Losses", key="h2"): go("performance")
        if st.button("Reports", key="h3"): go("performance")
        if st.button("Comparison", key="h4"): go("performance")

    with c2:
        st.markdown('<div class="main"><div class="main-title">Expected Data</div></div>', unsafe_allow_html=True)
        if st.button("Weather", key="h5"): go("expected")
        if st.button("Predictive Maintenance", key="h6"): go("expected")
        if st.button("Expected Energy Production", key="h7"): go("expected")
        if st.button("Best Time for Operation", key="h8"): go("expected")
        if st.button("Recommendations + Alerts", key="h9"): go("expected")

    with c3:
        st.markdown('<div class="main"><div class="main-title">Battery Status</div></div>', unsafe_allow_html=True)
        if st.button("Energy Inventory", key="h10"): go("battery")
        if st.button("Electrical Metrics", key="h11"): go("battery")
        if st.button("Battery Health", key="h12"): go("battery")

# ---------------- PERFORMANCE ----------------
elif st.session_state.page == "performance":

    st.markdown('<div class="title">Performance</div>', unsafe_allow_html=True)

    st.markdown('<div class="subtitle">Current Performance</div>', unsafe_allow_html=True)
    st.markdown('<div class="small">Current Output</div>', unsafe_allow_html=True)
    a,b,c = st.columns(3)
    a.metric("Current Energy","520 kW")
    b.metric("Production","1800 kWh")
    c.metric("Efficiency","94%")
    st.line_chart([320,380,430,500,540,510,470])

    st.markdown('<div class="subtitle">Profits / Losses</div>', unsafe_allow_html=True)
    a,b,c = st.columns(3)
    a.metric("Revenue","$12,400")
    b.metric("Profits","$8,100")
    c.metric("Losses","$1,240")
    st.bar_chart([4,6,7,8,10,12])

    st.markdown('<div class="subtitle">Reports</div>', unsafe_allow_html=True)
    r1,r2,r3 = st.columns(3)
    with r1:
        st.button("Daily", key="rd1")
        st.download_button("PDF", "Daily Report", file_name="daily.pdf")
    with r2:
        st.button("Weekly", key="rd2")
        st.download_button("PDF", "Weekly Report", file_name="weekly.pdf")
    with r3:
        st.button("Monthly", key="rd3")
        st.download_button("PDF", "Monthly Report", file_name="monthly.pdf")

    st.markdown('<div class="subtitle">Comparison</div>', unsafe_allow_html=True)

    st.write("Actual Power vs Expected Power")
    st.line_chart({"Actual":[420,510,490],"Expected":[450,520,505]})

    st.write("Today vs Yesterday")
    st.line_chart({"Today":[410,520,500],"Yesterday":[390,500,480]})

    st.write("This Month vs Last Month")
    st.bar_chart({"This Month":[12],"Last Month":[10]})

    st.write("Our System vs Ideal System")
    st.bar_chart({"Our":[94],"Ideal":[100]})

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
    st.line_chart({
        "Day 1":[34],
        "Day 2":[35],
        "Day 3":[33],
        "Day 4":[36]
    })

    st.markdown('<div class="subtitle">Predictive Maintenance</div>', unsafe_allow_html=True)
    st.file_uploader("Upload Panel Image")
    a,b = st.columns(2)
    a.metric("Clean Probability","78%")
    b.metric("Dusty Probability","22%")
    st.info("Recommendation: Light cleaning after 3 days.")

    st.markdown('<div class="subtitle">Expected Energy Production</div>', unsafe_allow_html=True)
    st.metric("Predicted Output","2100 kWh")
    st.write("Factors: Clear weather, panel cleanliness, battery availability, low shading.")

    st.markdown('<div class="subtitle">Best Time for Operation</div>', unsafe_allow_html=True)
    st.success("11:00 AM - 2:00 PM")
    st.write("Reason: Highest irradiation + lower battery stress + stable temperature.")

    st.markdown('<div class="subtitle">Recommendations + Alerts</div>', unsafe_allow_html=True)
    st.warning("Clean panels this week.")
    st.success("Run heavy loads between 11 AM and 2 PM.")

# ---------------- BATTERY ----------------
elif st.session_state.page == "battery":

    st.markdown('<div class="title">Battery Status</div>', unsafe_allow_html=True)

    st.markdown('<div class="subtitle">Energy Inventory</div>', unsafe_allow_html=True)
    a,b = st.columns(2)
    a.metric("Stored Energy","82%")
    b.metric("Available Capacity","18%")

    st.markdown('<div class="subtitle">Electrical Metrics</div>', unsafe_allow_html=True)
    a,b,c = st.columns(3)
    a.metric("Voltage","412 V")
    b.metric("Current","32 A")
    c.metric("Temp","31°C")

    st.markdown('<div class="subtitle">Battery Health</div>', unsafe_allow_html=True)
    a,b,c = st.columns(3)
    a.metric("Health","Healthy")
    b.metric("Cycles","1240")
    c.metric("Life Span","8.4 Years")
    st.line_chart([95,92,90,88,85,82])
