import streamlit as st
import pandas as pd
import requests
import time
BASE_URL = "https://shadow-residue-headcount.ngrok-free.dev"

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
    transition:.18s;
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
    transition:.15s;
}
div.stButton > button:hover{
    border-color:#f6b73c;
    color:#f6b73c;
}
.intro-wrap{
    height:92vh;
    display:flex;
    justify-content:center;
    align-items:center;
}

.intro-logo{
    font-size:78px;
    font-weight:900;
    font-style:italic;
    color:white;
    letter-spacing:4px;
    animation:introFade 2s ease forwards;
}

.intro-sun{
    color:#f6b73c;
    text-shadow:
    0 0 10px rgba(246,183,60,1),
    0 0 22px rgba(246,183,60,.7),
    0 0 38px rgba(246,183,60,.4);
}

@keyframes introFade{
    0%{opacity:0;transform:scale(.78);}
    35%{opacity:1;transform:scale(1);}
    70%{opacity:1;}
    100%{opacity:0;transform:scale(1.06);}
}
</style>
""", unsafe_allow_html=True)
if not st.session_state.intro_done:

    splash = st.empty()

    splash.markdown("""
    <div class="intro-wrap">
        <div class="intro-logo">
            NEX<span class="intro-sun">O</span>RA
        </div>
    </div>
    """, unsafe_allow_html=True)

    time.sleep(2)

    splash.empty()
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
        if st.button("Open Performance", key="open_perf"):
            go("performance")

    with c2:
        st.markdown("""
        <div class="main">
        <div class="main-title">Expected Data</div>
        <p>Weather, AI forecasts, maintenance insights.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Expected Data", key="open_exp"):
            go("expected")

    with c3:
        st.markdown("""
        <div class="main">
        <div class="main-title">Battery Status</div>
        <p>Inventory, health, voltage and cycles.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Battery", key="open_bat"):
            go("battery")

# ==================================================
# PERFORMANCE PAGE
# ==================================================
elif st.session_state.page == "performance":

    st.markdown('<div class="title">Performance</div>', unsafe_allow_html=True)

    # Current Performance
    st.markdown('<div class="subtitle">Current Performance</div>', unsafe_allow_html=True)

    a,b,c = st.columns(3)
    data = requests.get(f"{BASE_URL}/performance").json()

    a.metric("Current Power", f'{data["current_power"]} kW')
    b.metric("Production", f'{data["production"]} kWh')
    c.metric("Efficiency", f'{data["efficiency"]}%')

    st.markdown('<div class="subtitle">System Status</div>', unsafe_allow_html=True)
    st.success("Normal Operation")

    st.markdown('<div class="subtitle">AI Insight</div>', unsafe_allow_html=True)
    st.info("Performance increased due to strong irradiation and stable weather conditions.")

    st.markdown('<div class="subtitle">Live Graph - Last 24 Hours</div>', unsafe_allow_html=True)

    live_df = pd.DataFrame({
        "Hour":["00","03","06","09","12","15","18","21"],
        "Power":[0,0,80,320,560,470,140,0]
    })
    st.line_chart(live_df.set_index("Hour"))

    # Profits / Losses
    st.markdown('<div class="subtitle">Profits / Losses</div>', unsafe_allow_html=True)

    x,y,z = st.columns(3)
    x.metric("Revenue", "$12,400")
    y.metric("Profits", "$8,100")
    z.metric("Losses", "$1,240")

    st.markdown('<div class="subtitle">Status</div>', unsafe_allow_html=True)
    st.success("Profitable Performance")

    st.markdown('<div class="subtitle">AI Insight</div>', unsafe_allow_html=True)
    st.info("Higher profits were driven by increased daily production and lower maintenance load.")

    st.markdown('<div class="subtitle">Profit Summary</div>', unsafe_allow_html=True)

    profit_df = pd.DataFrame({
        "Month":["Jan","Feb","Mar","Apr","May","Jun"],
        "Profit":[4200,5100,4800,6200,7100,8100]
    })
    st.line_chart(profit_df.set_index("Month"))

    # Performance Comparing
    st.markdown('<div class="subtitle">Performance Comparing</div>', unsafe_allow_html=True)

    st.write("### Actual vs Expected")
    df1 = pd.DataFrame({
        "Hour":["06","08","10","12","14","16"],
        "Actual":[80,220,410,560,520,350],
        "Expected":[90,240,430,580,540,360]
    })
    st.line_chart(df1.set_index("Hour"))

    st.write("### Today vs Yesterday")
    df2 = pd.DataFrame({
        "Hour":["06","08","10","12","14","16"],
        "Today":[85,230,420,555,515,340],
        "Yesterday":[70,210,390,520,500,320]
    })
    st.line_chart(df2.set_index("Hour"))

    st.write("### This Month vs Last Month")
    df3 = pd.DataFrame({
        "Day":["1","5","10","15","20","25","30"],
        "This Month":[1650,1720,1800,1760,1840,1900,1950],
        "Last Month":[1500,1580,1620,1660,1700,1750,1800]
    })
    st.line_chart(df3.set_index("Day"))

    st.write("### Our System vs Ideal System")
    df4 = pd.DataFrame({
        "Hour":["06","08","10","12","14","16"],
        "Our System":[78,218,405,550,510,338],
        "Ideal System":[90,240,430,580,540,360]
    })
    st.line_chart(df4.set_index("Hour"))

    # Reports
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
elif st.session_state.page == "expected":
exp = requests.get(f"{BASE_URL}/expected-data").json()
    st.markdown('<div class="title">Expected Data</div>', unsafe_allow_html=True)

    # --------------------------------
    # Weather
    # --------------------------------
    st.markdown('<div class="subtitle">Weather</div>', unsafe_allow_html=True)

    a,b,c,d = st.columns(4)
    a.metric("Temperature", f'{exp["temperature"]}°C')
    b.metric("Irradiation", f'{exp["irradiation"]} W/m²')
    c.metric("Wind Speed", f'{exp["wind_speed"]} km/h')
    d.metric("Humidity", f'{exp["humidity"]}%')

    weather_df = pd.DataFrame({
        "Day":["Day1","Day2","Day3","Day4"],
        "Temp":[34,35,33,36],
        "Rain":[10,15,5,0],
        "Wind":[9,12,8,10],
        "Clouds":[20,35,15,10],
        "Irradiation":[920,880,950,980]
    })

    st.line_chart(weather_df.set_index("Day"))

    # --------------------------------
    # Predictive Maintenance
    # --------------------------------
    st.markdown('<div class="subtitle">Predictive Maintenance</div>', unsafe_allow_html=True)

    x,y,z = st.columns(3)
    x.metric("Failure Risk", "18%")
    y.metric("Risk Level", "Low")
    z.metric("Health Score", "91%")

    st.success("Status: Stable Condition")

    st.markdown("### AI Insight")
    st.info("System components are operating normally. No immediate maintenance required.")

    st.markdown("### Panel Image Upload")
    st.file_uploader("Upload Panel Image", type=["png","jpg","jpeg"])

    c1,c2 = st.columns(2)
    c1.metric("Clean", "78%")
    c2.metric("Dusty", "22%")

    st.write("Confidence: 92%")

    # --------------------------------
    # Expected Energy Production
    # --------------------------------
    st.markdown('<div class="subtitle">Expected Energy Production</div>', unsafe_allow_html=True)

    p1,p2 = st.columns(2)
    p1.metric("Expected Next Day Production", "2100 kWh")
    p2.metric("Expected Weekly Average", "1980 kWh")

    # --------------------------------
    # Best Time for Operation
    # --------------------------------
    st.markdown('<div class="subtitle">Best Time for Operation</div>', unsafe_allow_html=True)

    st.success("11:00 AM - 2:00 PM")
    st.write("Reason: Highest expected solar irradiation.")

    # --------------------------------
    # Recommendations + Alerts
    # --------------------------------
    st.markdown('<div class="subtitle">Recommendations + Alerts</div>', unsafe_allow_html=True)

    st.success("Operate heavy loads during noon hours.")
    st.warning("Inspect panel surface this week for minor dust accumulation.")
    st.info("Weather conditions favorable for strong energy production.")
elif st.session_state.page == "battery":
bat = requests.get(f"{BASE_URL}/battery-status").json()
    st.markdown('<div class="title">Battery Status</div>', unsafe_allow_html=True)

    # --------------------------------
    # Energy Inventory
    # --------------------------------
    st.markdown('<div class="subtitle">Energy Inventory</div>', unsafe_allow_html=True)

    a,b = st.columns(2)
    a.metric("Battery Level", f'{bat["battery_level"]}%')
    b.metric("Stored Energy", f'{bat["stored_energy"]} kWh')

    # --------------------------------
    # Battery Health Metrics
    # --------------------------------
    st.markdown('<div class="subtitle">Battery Health Metrics</div>', unsafe_allow_html=True)

    x,y,z = st.columns(3)
    x.metric("Voltage", f'{bat["voltage"]} V')
    y.metric("Current", f'{bat["current"]} A')
    z.metric("Temp", f'{bat["temperature"]}°C')

    # --------------------------------
    # Battery Status
    # --------------------------------
    st.markdown('<div class="subtitle">Battery Status</div>', unsafe_allow_html=True)

    st.success("Healthy")

    st.markdown("### AI Insight")
    st.info("Battery operating within optimal range. Stable temperature and healthy charge retention detected.")

    # --------------------------------
    # Battery Level Trend
    # --------------------------------
    st.markdown('<div class="subtitle">Battery Level Trend</div>', unsafe_allow_html=True)

    trend_df = pd.DataFrame({
        "Recent Readings":["1","2","3","4","5","6"],
        "Battery %":[95,92,90,88,85,82]
    })

    st.line_chart(trend_df.set_index("Recent Readings"))

    # --------------------------------
    # Battery Mode
    # --------------------------------
    st.markdown('<div class="subtitle">Battery Mode</div>', unsafe_allow_html=True)

    st.info("Charging Detected")

    # --------------------------------
    # Remaining Time Estimate
    # --------------------------------
    st.markdown('<div class="subtitle">Remaining Time Estimate</div>', unsafe_allow_html=True)

    st.write("Estimated Runtime: 6.4 Hours")

    # --------------------------------
    # Battery Alerts
    # --------------------------------
    st.markdown('<div class="subtitle">Battery Alerts</div>', unsafe_allow_html=True)

    st.success("No critical alerts detected.")

    # --------------------------------
    # Health Degradation Forecast
    # --------------------------------
    st.markdown('<div class="subtitle">Health Degradation Forecast</div>', unsafe_allow_html=True)

    c1,c2 = st.columns(2)
    c1.metric("Predicted Future Battery Health", "87%")
    c2.metric("Forecast Status", "Normal Aging")
