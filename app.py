import streamlit as st
import pandas as pd

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
</style>
""", unsafe_allow_html=True)

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

    # --------------------------------
    # Current Performance
    # --------------------------------
    st.markdown('<div class="subtitle">Current Performance</div>', unsafe_allow_html=True)

    a,b,c = st.columns(3)
    a.metric("Current Power", "520 kW")
    b.metric("Production", "1800 kWh")
    c.metric("Efficiency", "94%")

    # --------------------------------
    # System Status
    # --------------------------------
    st.markdown('<div class="subtitle">System Status</div>', unsafe_allow_html=True)
    st.success("Normal Operation")

    # --------------------------------
    # AI Insight
    # --------------------------------
    st.markdown('<div class="subtitle">AI Insight</div>', unsafe_allow_html=True)

    st.info("""
Performance increased today due to strong solar irradiation,
low cloud cover, and stable panel temperature.
No abnormal efficiency drop detected.
""")

    # --------------------------------
    # Live Graph - Last 24 Hours
    # --------------------------------
    st.markdown('<div class="subtitle">Live Graph - Last 24 Hours</div>', unsafe_allow_html=True)

    chart_df = pd.DataFrame({
        "Time":[
            "00","01","02","03","04","05","06","07","08","09","10","11",
            "12","13","14","15","16","17","18","19","20","21","22","23"
        ],
        "Power":[
            0,0,0,0,5,20,80,160,260,390,470,530,
            560,545,520,480,410,300,180,70,10,0,0,0
        ]
    })

    st.line_chart(chart_df.set_index("Time"))
 # --------------------------------
# Profits / Losses
# --------------------------------
st.markdown('<div class="subtitle">Profits / Losses</div>', unsafe_allow_html=True)

x,y,z = st.columns(3)
x.metric("Revenue", "$12,400")
y.metric("Profits", "$8,100")
z.metric("Losses", "$1,240")

# Status
st.markdown('<div class="subtitle">Status</div>', unsafe_allow_html=True)
st.success("Profitable Performance")

# AI Insight
st.markdown('<div class="subtitle">AI Insight</div>', unsafe_allow_html=True)

st.info("""
Profit increased this period due to higher energy production,
stable operating efficiency, and reduced maintenance costs.
Losses remained within acceptable range.
""")

# Profit Graph
st.markdown('<div class="subtitle">Profit Summary</div>', unsafe_allow_html=True)

st.write("### Profit Trend")
profit_df = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May","Jun"],
    "Profit":[4200,5100,4800,6200,7100,8100]
})

st.line_chart(profit_df.set_index("Month"))

    # --------------------------------
# Performance Comparing
# --------------------------------
st.markdown('<div class="subtitle">Performance Comparing</div>', unsafe_allow_html=True)

# Actual vs Expected
st.write("### Actual vs Expected")
df1 = pd.DataFrame({
    "Hour":["06","08","10","12","14","16","18"],
    "Actual":[80,220,410,560,520,350,120],
    "Expected":[90,240,430,580,540,360,130]
})
st.line_chart(df1.set_index("Hour"))

# Today vs Yesterday
st.write("### Today vs Yesterday")
df2 = pd.DataFrame({
    "Hour":["06","08","10","12","14","16","18"],
    "Today":[85,230,420,555,515,340,110],
    "Yesterday":[70,210,390,520,500,320,100]
})
st.line_chart(df2.set_index("Hour"))

# This Month vs Last Month
st.write("### This Month vs Last Month")
df3 = pd.DataFrame({
    "Day":["1","5","10","15","20","25","30"],
    "This Month":[1650,1720,1800,1760,1840,1900,1950],
    "Last Month":[1500,1580,1620,1660,1700,1750,1800]
})
st.line_chart(df3.set_index("Day"))

# Our System vs Ideal System
st.write("### Our System vs Ideal System")
df4 = pd.DataFrame({
    "Hour":["06","08","10","12","14","16","18"],
    "Our System":[78,218,405,550,510,338,115],
    "Ideal System":[90,240,430,580,540,360,130]
})
st.line_chart(df4.set_index("Hour"))

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
    st.write("Factors:")
    st.write("- Weather quality")
    st.write("- Panel cleanliness")
    st.write("- Battery availability")
    st.write("- Low shading")

    st.markdown('<div class="subtitle">Best Time for Operation</div>', unsafe_allow_html=True)

    st.success("11:00 AM - 2:00 PM")
    st.write("Reason: highest irradiation and stable temperature.")

    st.markdown('<div class="subtitle">Recommendations + Alerts</div>', unsafe_allow_html=True)

    st.warning("Clean panels this week.")
    st.success("Run heavy loads near noon.")

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

    st.markdown('<div class="subtitle">Battery Health</div>', unsafe_allow_html=True)

    x,y,z = st.columns(3)
    x.metric("Health","Healthy")
    y.metric("Cycles","1240")
    z.metric("Life Span","8.4 Years")

    st.line_chart(pd.DataFrame({
        "Charge %":[95,92,90,88,85,82]
    }))
