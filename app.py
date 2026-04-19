import streamlit as st
import time

st.set_page_config(page_title="Nexora Solar", page_icon="☀️", layout="wide")

# ---------- STATE ----------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "splash_done" not in st.session_state:
    st.session_state.splash_done = False

def go(page):
    st.session_state.page = page
    st.rerun()

# ---------- STYLE ----------
st.markdown("""
<style>
html,body,[class*="css"]{
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
color:white;
letter-spacing:2px;
}
.sun{
color:#f6b73c;
text-shadow:0 0 18px rgba(246,183,60,.65);
}

.hero{text-align:center;padding-top:60px;padding-bottom:35px;}
.hero h1{font-size:74px;font-weight:900;line-height:1.08;}
.gold{color:#f6b73c;}

.desc{
max-width:980px;
margin:auto;
font-size:20px;
line-height:1.7;
color:#d5d5d5;
}

.stat{
background:#111;
border:1px solid #222;
border-radius:18px;
padding:26px;
height:155px;
text-align:center;
}
.stat h2{margin:0;font-size:42px;color:#f6b73c;}
.stat p{margin-top:8px;color:#ccc;}

.mainbox{
background:#101010;
border:1px solid #222;
border-radius:22px;
padding:24px;
min-height:320px;
transition:.3s;
animation:rise .8s ease;
}
.mainbox:hover{
transform:translateY(-10px);
border-color:#f6b73c;
box-shadow:0 0 20px rgba(246,183,60,.14);
}
@keyframes rise{
from{opacity:0;transform:translateY(35px);}
to{opacity:1;transform:translateY(0);}
}

.title{
font-size:50px;
font-weight:900;
color:#f6b73c;
margin-top:20px;
margin-bottom:20px;
}

.subtitle{
font-size:34px;
font-weight:800;
color:white;
margin-top:10px;
margin-bottom:10px;
}

.small{
font-size:18px;
color:#d5d5d5;
line-height:1.8;
}

.glowbtn button{
background:#f6b73c !important;
color:black !important;
font-weight:900 !important;
border:none !important;
animation:pulse 2s infinite;
}
@keyframes pulse{
50%{box-shadow:0 0 20px rgba(246,183,60,.45);}
}

.splash{
height:85vh;
display:flex;
justify-content:center;
align-items:center;
font-size:74px;
font-weight:900;
font-style:italic;
color:white;
letter-spacing:3px;
animation:pop .8s ease;
}
@keyframes pop{
from{transform:scale(.7);opacity:0;}
to{transform:scale(1);opacity:1;}
}
</style>
""", unsafe_allow_html=True)

# ---------- SPLASH ----------
if not st.session_state.splash_done:
    st.markdown("""
    <div class="splash">
    NEX<span class="sun">O</span>RA
    </div>
    """, unsafe_allow_html=True)
    time.sleep(2)
    st.session_state.splash_done = True
    st.rerun()

# ---------- TOP ----------
a,b = st.columns([8,1])

with a:
    st.markdown('<div class="logo">NEX<span class="sun">O</span>RA</div>', unsafe_allow_html=True)

with b:
    with st.popover("☰"):
        if st.button("Performance"): go("performance_menu")
        if st.button("Expected Data"): go("expected_menu")
        if st.button("Battery Status"): go("battery_menu")
        if st.button("Current Performance"): go("current")
        if st.button("Recommendations + Alerts"): go("recommend")

# ---------- HOME ----------
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

    st.markdown('<div class="glowbtn">', unsafe_allow_html=True)
    if st.button("Let's Start Today →"):
        go("current")
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("")

    s1,s2,s3,s4 = st.columns(4)
    vals=[("15K+","Installations"),("98+","Projects Completed"),("40%","Avg. Cost Saving"),("12","Years Experience")]

    for col,(n,t) in zip([s1,s2,s3,s4],vals):
        with col:
            st.markdown(f'<div class="stat"><h2>{n}</h2><p>{t}</p></div>', unsafe_allow_html=True)

    st.write("")
    c1,c2,c3 = st.columns(3)

    with c1:
        st.markdown('<div class="mainbox"><div class="title" style="font-size:30px;">Performance</div></div>', unsafe_allow_html=True)
        if st.button("Current Performance"): go("current")
        if st.button("Profits / Losses"): go("profits")
        if st.button("Reports"): go("reports")
        if st.button("Comparison"): go("compare")

    with c2:
        st.markdown('<div class="mainbox"><div class="title" style="font-size:30px;">Expected Data</div></div>', unsafe_allow_html=True)
        if st.button("Weather"): go("weather")
        if st.button("Predictive Maintenance"): go("maint")
        if st.button("Expected Energy Production"): go("energy")
        if st.button("Best Time for Operation"): go("best")
        if st.button("Recommendations + Alerts"): go("recommend")

    with c3:
        st.markdown('<div class="mainbox"><div class="title" style="font-size:30px;">Battery Status</div></div>', unsafe_allow_html=True)
        if st.button("Energy Inventory"): go("inventory")
        if st.button("Electrical Metrics"): go("metrics")
        if st.button("Battery Status"): go("battery")

# ---------- PERFORMANCE MENU ----------
elif st.session_state.page == "performance_menu":
    st.markdown('<div class="title">Performance</div>', unsafe_allow_html=True)
    if st.button("Current Performance"): go("current")
    if st.button("Profits / Losses"): go("profits")
    if st.button("Reports"): go("reports")
    if st.button("Comparison"): go("compare")

elif st.session_state.page == "current":
    st.markdown('<div class="title">Performance</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Current Output</div>', unsafe_allow_html=True)
    st.markdown('<div class="small">Current Energy: 520 kW<br>Production: 1800 kWh<br>Efficiency: 94%</div>', unsafe_allow_html=True)
    st.write("")
    st.line_chart([320,380,430,500,540,510,470,420])

elif st.session_state.page == "profits":
    st.markdown('<div class="title">Profits / Losses</div>', unsafe_allow_html=True)
    a,b,c=st.columns(3)
    a.metric("Revenue","$12,400")
    b.metric("Profits","$8,100")
    c.metric("Losses","$1,240")

elif st.session_state.page == "reports":
    st.markdown('<div class="title">Reports</div>', unsafe_allow_html=True)
    st.button("Daily")
    st.button("Weekly")
    st.button("Monthly")
    st.download_button("PDF Download","Report","report.pdf")

elif st.session_state.page == "compare":
    st.markdown('<div class="title">Comparison</div>', unsafe_allow_html=True)
    st.line_chart({"Actual":[420,510,490],"Expected":[450,520,505]})

# ---------- EXPECTED ----------
elif st.session_state.page == "expected_menu":
    st.markdown('<div class="title">Expected Data</div>', unsafe_allow_html=True)
    if st.button("Weather"): go("weather")
    if st.button("Predictive Maintenance"): go("maint")
    if st.button("Expected Energy Production"): go("energy")
    if st.button("Best Time for Operation"): go("best")
    if st.button("Recommendations + Alerts"): go("recommend")

elif st.session_state.page == "weather":
    st.markdown('<div class="title">Expected Data</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Weather</div>', unsafe_allow_html=True)
    a,b,c,d,e=st.columns(5)
    a.metric("Temp","34°C")
    b.metric("Humidity","48%")
    c.metric("Cloud Cover","15%")
    d.metric("Wind Speed","9 km/h")
    e.metric("Irradiation","920 W/m²")

elif st.session_state.page == "maint":
    st.markdown('<div class="title">Expected Data</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Predictive Maintenance</div>', unsafe_allow_html=True)
    st.file_uploader("Upload Panel Image")
    st.info("Light dust detected. Cleaning recommended.")

elif st.session_state.page == "energy":
    st.markdown('<div class="title">Expected Data</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Expected Energy Production</div>', unsafe_allow_html=True)
    st.metric("Predicted Output","2100 kWh")

elif st.session_state.page == "best":
    st.markdown('<div class="title">Expected Data</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Best Time for Operation</div>', unsafe_allow_html=True)
    st.success("11:00 AM - 2:00 PM")

elif st.session_state.page == "recommend":
    st.markdown('<div class="title">Expected Data</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Recommendations + Alerts</div>', unsafe_allow_html=True)
    st.warning("Clean panels this week.")
    st.success("Battery charging optimized for tomorrow.")

# ---------- BATTERY ----------
elif st.session_state.page == "battery_menu":
    st.markdown('<div class="title">Battery Status</div>', unsafe_allow_html=True)
    if st.button("Energy Inventory"): go("inventory")
    if st.button("Electrical Metrics"): go("metrics")
    if st.button("Battery Status"): go("battery")

elif st.session_state.page == "inventory":
    st.markdown('<div class="title">Battery Status</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Energy Inventory</div>', unsafe_allow_html=True)
    st.metric("Stored Energy","82%")
    st.metric("Available Capacity","18%")

elif st.session_state.page == "metrics":
    st.markdown('<div class="title">Battery Status</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Electrical Metrics</div>', unsafe_allow_html=True)
    a,b,c=st.columns(3)
    a.metric("Voltage","412 V")
    b.metric("Current","32 A")
    c.metric("Temp","31°C")

elif st.session_state.page == "battery":
    st.markdown('<div class="title">Battery Status</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">System Health</div>', unsafe_allow_html=True)
    a,b,c=st.columns(3)
    a.metric("Health","Healthy")
    b.metric("Cycles","1240")
    c.metric("Life Span","8.4 Years")
    st.line_chart([95,92,89,86,84,82])

# ---------- BACK ----------
st.write("")
if st.session_state.page != "home":
    if st.button("← Back to Home"):
        go("home")
