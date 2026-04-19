import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Nexora Solar", page_icon="☀️", layout="wide")

# ---------------- STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "report_type" not in st.session_state:
    st.session_state.report_type = "Daily"

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
font-size:38px;
font-weight:900;
font-style:italic;
color:white;
letter-spacing:2px;
}
.sun{
color:#f6b73c;
text-shadow:
0 0 6px rgba(246,183,60,.7),
0 0 12px rgba(246,183,60,.5),
0 0 18px rgba(246,183,60,.35);
}

.hero{
text-align:center;
padding:55px 0 35px 0;
}

.hero h1{
font-size:72px;
font-weight:900;
line-height:1.08;
}

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
box-shadow:0 0 12px rgba(246,183,60,.08);
animation:pulsebox 2.8s infinite;
transition:.25s;
}
.main:hover{
transform:translateY(-8px);
border-color:#f6b73c;
}

@keyframes pulsebox{
50%{box-shadow:0 0 18px rgba(246,183,60,.18);}
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

.reportbox{
background:#111;
border:1px solid #222;
border-radius:18px;
padding:20px;
margin-top:12px;
}

.splash{
height:90vh;
display:flex;
justify-content:center;
align-items:center;
font-size:68px;
font-weight:900;
font-style:italic;
color:white;
opacity:0;
animation:fadeall 2s ease forwards;
}

@keyframes fadeall{
0%{opacity:0;transform:scale(.8);}
35%{opacity:1;transform:scale(1);}
70%{opacity:1;}
100%{opacity:0;transform:scale(1.04);}
}

.splashsun{
color:#f6b73c;
text-shadow:
0 0 8px rgba(246,183,60,.9),
0 0 16px rgba(246,183,60,.6),
0 0 26px rgba(246,183,60,.35);
}
</style>
""", unsafe_allow_html=True)

# ---------------- SPLASH (EVERY REFRESH) ----------------
placeholder = st.empty()
placeholder.markdown("""
<div class="splash">
NEX<span class="splashsun">O</span>RA
</div>
""", unsafe_allow_html=True)
time.sleep(2)
placeholder.empty()

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
    <h1>Where Energy Is <span class="gold">Managed</span><br>Not Wasted</h1>
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
        st.markdown('<div class="main"><div class="main-title">Performance</div></div>', unsafe_allow_html=True)
        if st.button("Open Performance"): go("performance")

    with c2:
        st.markdown('<div class="main"><div class="main-title">Expected Data</div></div>', unsafe_allow_html=True)
        if st.button("Open Expected Data"): go("expected")

    with c3:
        st.markdown('<div class="main"><div class="main-title">Battery Status</div></div>', unsafe_allow_html=True)
        if st.button("Open Battery"): go("battery")

# ---------------- PERFORMANCE ----------------
elif st.session_state.page == "performance":

    st.markdown('<div class="title">Performance</div>', unsafe_allow_html=True)

    st.markdown('<div class="subtitle">Current Performance</div>', unsafe_allow_html=True)
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

    st.markdown('<div class="subtitle">Comparison</div>', unsafe_allow_html=True)

    st.write("Actual Power vs Expected Power")
    st.line_chart({"Actual":[420,510,490],"Expected":[450,520,505]})

    st.write("Today vs Yesterday")
    st.line_chart({"Today":[410,520,500],"Yesterday":[390,500,480]})

    st.write("This Month vs Last Month")
    st.bar_chart({"This Month":[12],"Last Month":[10]})

    st.write("Our System vs Ideal System")
    st.bar_chart({"Our":[94],"Ideal":[100]})

    # reports last
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
    Energy Output: Good<br>
    Efficiency: Stable<br>
    Revenue Trend: Positive<br>
    Recommended Action: Continue Monitoring
    </div>
    """, unsafe_allow_html=True)

    st.download_button(
        "Download PDF",
        data=f"{st.session_state.report_type} Report",
        file_name=f"{st.session_state.report_type.lower()}_report.pdf"
    )

# ---------------- EXPECTED ----------------
elif st.session_state.page == "expected":

    st.markdown('<div class="title">Expected Data</div>', unsafe_allow_html=True)

    st.markdown('<div class="subtitle">Weather</div>', unsafe_allow_html=True)
    st.line_chart({
        "Day 1":[34],
        "Day 2":[35],
        "Day 3":[33],
        "Day 4":[36]
    })

    st.markdown('<div class="subtitle">Predictive Maintenance</div>', unsafe_allow_html=True)
    st.file_uploader("Upload Panel Image")
    a,b = st.columns(2)
    a.metric("Clean","78%")
    b.metric("Dusty","22%")
    st.info("Light cleaning recommended.")

    st.markdown('<div class="subtitle">Expected Energy Production</div>', unsafe_allow_html=True)
    st.write("Predicted Output: 2100 kWh")
    st.write("Factors: Weather / Panel Cleanliness / Battery Capacity / Low Shading")

    st.markdown('<div class="subtitle">Best Time for Operation</div>', unsafe_allow_html=True)
    st.success("11 AM - 2 PM")
    st.write("Highest solar irradiation + stable temperature.")

    st.markdown('<div class="subtitle">Recommendations + Alerts</div>', unsafe_allow_html=True)
    st.warning("Clean panels this week.")
    st.success("Run heavy loads at noon.")

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
