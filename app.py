import streamlit as st
import pandas as pd
import time

st.set_page_config(
    page_title="Nexora Solar",
    page_icon="☀️",
    layout="wide"
)

# ---------------------------
# SESSION STATE
# ---------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "intro_done" not in st.session_state:
    st.session_state.intro_done = False

def go(page_name):
    st.session_state.page = page_name
    st.rerun()

# ---------------------------
# STYLE
# ---------------------------
st.markdown("""
<style>
html, body, [class*="css"]{
    background:#050505;
    color:white;
    font-family:Arial,sans-serif;
}

header,#MainMenu,footer{
    visibility:hidden;
}

.block-container{
    max-width:1450px;
    padding-top:1rem;
    padding-left:2rem;
    padding-right:2rem;
}

/* Logo */
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

/* INTRO */
.intro-wrap{
    height:88vh;
    display:flex;
    justify-content:center;
    align-items:center;
}
.intro-logo{
    font-size:72px;
    font-weight:900;
    font-style:italic;
    color:white;
    letter-spacing:4px;
    animation:introFade 2s ease forwards;
}
.intro-sun{
    color:#f6b73c;
    text-shadow:
    0 0 8px rgba(246,183,60,.95),
    0 0 18px rgba(246,183,60,.65),
    0 0 30px rgba(246,183,60,.35);
}
@keyframes introFade{
    0%{opacity:0;transform:scale(.78);}
    35%{opacity:1;transform:scale(1);}
    70%{opacity:1;}
    100%{opacity:0;transform:scale(1.06);}
}

/* Hero */
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

/* Stats */
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

/* Main Cards */
.main{
    background:#101010;
    border:1px solid #222;
    border-radius:20px;
    padding:18px;
    min-height:220px;
    transition:.12s;
    box-shadow:0 0 10px rgba(246,183,60,.05);
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

/* Fake clickable full card button */
.cardbtn button{
    width:100%;
    height:220px;
    opacity:0;
    margin-top:-220px;
}

/* Section titles */
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

/* Buttons */
div.stButton > button{
    width:100%;
    border-radius:12px;
    border:1px solid #333;
    background:#111;
    color:white;
    transition:.12s;
}
div.stButton > button:hover{
    border-color:#f6b73c;
    color:#f6b73c;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# INTRO SPLASH
# ---------------------------
if not st.session_state.intro_done:
    st.markdown("""
    <div class="intro-wrap">
        <div class="intro-logo">
            NEX<span class="intro-sun">O</span>RA
        </div>
    </div>
    """, unsafe_allow_html=True)
    time.sleep(2)
    st.session_state.intro_done = True
    st.rerun()

# ---------------------------
# TOP BAR
# ---------------------------
a,b = st.columns([8,1])

with a:
    st.markdown(
        '<div class="logo">NEX<span class="sun">O</span>RA</div>',
        unsafe_allow_html=True
    )

with b:
    with st.popover("☰"):
        if st.button("Home", key="nav_home"):
            go("home")
        if st.button("Performance", key="nav_perf"):
            go("performance")
        if st.button("Expected Data", key="nav_exp"):
            go("expected")
        if st.button("Battery Status", key="nav_bat"):
            go("battery")

# ---------------------------
# BACK BUTTON
# ---------------------------
if st.session_state.page != "home":
    c1,c2 = st.columns([8,1])
    with c2:
        if st.button("← Back", key="back_home"):
            go("home")

# ==================================================
# HOME PAGE
# ==================================================
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

    if st.button("Let's Start Today →", key="start_now"):
        go("performance")

    s1,s2,s3,s4 = st.columns(4)

    stats = [
        ("15K+","Installations"),
        ("98+","Projects"),
        ("40%","Saving"),
        ("12","Years")
    ]

    for col,(num,text) in zip([s1,s2,s3,s4],stats):
        with col:
            st.markdown(
                f'<div class="stat"><h2>{num}</h2><p>{text}</p></div>',
                unsafe_allow_html=True
            )

    st.write("")
    st.write("")

    c1,c2,c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="main">
        <div class="main-title">Performance</div>
        <p>Monitoring, reports, profits, comparisons.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<div class="cardbtn">', unsafe_allow_html=True)
        if st.button("Performance", key="card_perf"):
            go("performance")
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="main">
        <div class="main-title">Expected Data</div>
        <p>Weather, AI forecasts, maintenance insights.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<div class="cardbtn">', unsafe_allow_html=True)
        if st.button("Expected Data", key="card_exp"):
            go("expected")
        st.markdown('</div>', unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="main">
        <div class="main-title">Battery Status</div>
        <p>Inventory, health, voltage and cycles.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<div class="cardbtn">', unsafe_allow_html=True)
        if st.button("Battery Status", key="card_bat"):
            go("battery")
        st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# PERFORMANCE PAGE
# ==================================================
elif st.session_state.page == "performance":

    st.markdown('<div class="title">Performance</div>', unsafe_allow_html=True)

    st.markdown('<div class="subtitle">Current Performance</div>', unsafe_allow_html=True)

    a,b,c = st.columns(3)
    a.metric("Current Energy","520 kW")
    b.metric("Production","1800 kWh")
    c.metric("Efficiency","94%")

    st.write("Live Output Graph - Last 24 Hours")
    st.line_chart(
        pd.DataFrame({
            "kW":[220,250,270,290,310,340,370,410,450,500,530,550,
                  560,540,520,500,470,430,390,350,320,290,260,230]
        })
    )

    st.markdown('<div class="subtitle">Profits / Losses</div>', unsafe_allow_html=True)

    x,y,z = st.columns(3)
    x.metric("Revenue","$12,400")
    y.metric("Profits","$8,100")
    z.metric("Losses","$1,240")

    st.bar_chart(pd.DataFrame({"USD":[3,5,6,8,7,9,12]}))

    st.markdown('<div class="subtitle">Comparison</div>', unsafe_allow_html=True)

    st.write("Actual vs Expected")
    st.line_chart(pd.DataFrame({
        "Actual":[420,510,490,530],
        "Expected":[450,520,505,540]
    }))

    st.markdown('<div class="subtitle">Reports</div>', unsafe_allow_html=True)

    r1,r2,r3 = st.columns(3)

    with r1:
        st.button("Daily", key="daily_report")
        st.download_button("PDF", "Daily Report", file_name="daily.pdf")

    with r2:
        st.button("Weekly", key="weekly_report")
        st.download_button("PDF", "Weekly Report", file_name="weekly.pdf")

    with r3:
        st.button("Monthly", key="monthly_report")
        st.download_button("PDF", "Monthly Report", file_name="monthly.pdf")

# ==================================================
# EXPECTED DATA PAGE
# ==================================================
elif st.session_state.page == "expected":

    st.markdown('<div class="title">Expected Data</div>', unsafe_allow_html=True)

    st.markdown('<div class="subtitle">Weather</div>', unsafe_allow_html=True)

    a,b,c,d,e = st.columns(5)
    a.metric("Temperature","34°C")
    b.metric("Humidity","48%")
    c.metric("Cloud Cover","15%")
    d.metric("Irradiation","920 W/m²")
    e.metric("Wind Speed","9 km/h")

    st.line_chart(pd.DataFrame({
        "Temp":[34,35,33,36]
    }, index=["Day1","Day2","Day3","Day4"]))

    st.markdown('<div class="subtitle">Predictive Maintenance</div>', unsafe_allow_html=True)

    st.file_uploader("Upload Panel Image", type=["png","jpg","jpeg"])

    q1,q2 = st.columns(2)
    q1.metric("Clean Probability","78%")
    q2.metric("Dusty Probability","22%")

    st.info("Recommendation: Light cleaning recommended.")

    st.markdown('<div class="subtitle">Expected Energy Production</div>', unsafe_allow_html=True)

    st.write("Predicted Output: 2100 kWh")

# ==================================================
# BATTERY PAGE
# ==================================================
elif st.session_state.page == "battery":

    st.markdown('<div class="title">Battery Status</div>', unsafe_allow_html=True)

    st.markdown('<div class="subtitle">Energy Inventory</div>', unsafe_allow_html=True)

    p1,p2 = st.columns(2)
    p1.metric("Stored Energy","82%")
    p2.metric("Available Capacity","18%")

    st.markdown('<div class="subtitle">Electrical Metrics</div>', unsafe_allow_html=True)

    a,b,c = st.columns(3)
    a.metric("Voltage","412 V")
    b.metric("Current","32 A")
    c.metric("Temp","31°C")
