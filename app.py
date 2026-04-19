import streamlit as st
import time

st.set_page_config(page_title="Nexora Solar", page_icon="☀️", layout="wide")

# ---------------- STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "splash_done" not in st.session_state:
    st.session_state.splash_done = False

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
.block-container{max-width:1450px;padding:1rem 2rem;}

.logo{
font-size:44px;
font-weight:900;
font-style:italic;
color:white;
letter-spacing:2px;
}
.sun{
color:#f6b73c;
text-shadow:0 0 16px rgba(246,183,60,.6);
}

.hero{text-align:center;padding:60px 0 35px 0;}
.hero h1{font-size:72px;font-weight:900;line-height:1.08;}
.gold{color:#f6b73c;}

.desc{
max-width:960px;
margin:auto;
font-size:20px;
line-height:1.7;
color:#d5d5d5;
}

.card{
background:#101010;
border:1px solid #222;
border-radius:20px;
padding:25px;
height:160px;
text-align:center;
}

.card h2{
margin:0;
font-size:42px;
color:#f6b73c;
}

.main{
background:#101010;
border:1px solid #222;
border-radius:22px;
padding:24px;
min-height:320px;
transition:.25s;
}
.main:hover{
transform:translateY(-10px);
border-color:#f6b73c;
}

.title{
font-size:48px;
font-weight:900;
color:#f6b73c;
margin:20px 0;
}

.subtitle{
font-size:30px;
font-weight:800;
margin:15px 0;
}

.splash{
height:85vh;
display:flex;
justify-content:center;
align-items:center;
font-size:74px;
font-weight:900;
font-style:italic;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SPLASH ----------------
if not st.session_state.splash_done:
    st.markdown('<div class="splash">NEX<span class="sun">O</span>RA</div>', unsafe_allow_html=True)
    time.sleep(2)
    st.session_state.splash_done = True
    st.rerun()

# ---------------- TOP ----------------
a,b = st.columns([8,1])
with a:
    st.markdown('<div class="logo">NEX<span class="sun">O</span>RA</div>', unsafe_allow_html=True)

with b:
    with st.popover("☰"):
        if st.button("Performance", key="nav1"): go("performance")
        if st.button("Expected Data", key="nav2"): go("expected")
        if st.button("Battery Status", key="nav3"): go("battery")

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
        go("current")

    c1,c2,c3,c4 = st.columns(4)
    nums=[("15K+","Installations"),("98+","Projects"),("40%","Saving"),("12","Years")]
    for col,(n,t) in zip([c1,c2,c3,c4],nums):
        with col:
            st.markdown(f'<div class="card"><h2>{n}</h2><p>{t}</p></div>', unsafe_allow_html=True)

    st.write("")
    x1,x2,x3 = st.columns(3)

    with x1:
        st.markdown('<div class="main"><div class="title" style="font-size:28px;">Performance</div></div>', unsafe_allow_html=True)
        if st.button("Current Performance", key="h1"): go("current")
        if st.button("Profits / Losses", key="h2"): go("profits")
        if st.button("Reports", key="h3"): go("reports")
        if st.button("Comparison", key="h4"): go("compare")

    with x2:
        st.markdown('<div class="main"><div class="title" style="font-size:28px;">Expected Data</div></div>', unsafe_allow_html=True)
        if st.button("Weather", key="h5"): go("weather")
        if st.button("Predictive Maintenance", key="h6"): go("maint")
        if st.button("Expected Energy Production", key="h7"): go("energy")
        if st.button("Best Time for Operation", key="h8"): go("best")
        if st.button("Recommendations + Alerts", key="h9"): go("recommend")

    with x3:
        st.markdown('<div class="main"><div class="title" style="font-size:28px;">Battery Status</div></div>', unsafe_allow_html=True)
        if st.button("Energy Inventory", key="h10"): go("inventory")
        if st.button("Electrical Metrics", key="h11"): go("metrics")
        if st.button("Battery Health", key="h12"): go("battery")

# ---------------- PERFORMANCE ----------------
elif st.session_state.page == "performance":
    st.markdown('<div class="title">Performance</div>', unsafe_allow_html=True)
    if st.button("Current Performance", key="p1"): go("current")
    if st.button("Profits / Losses", key="p2"): go("profits")
    if st.button("Reports", key="p3"): go("reports")
    if st.button("Comparison", key="p4"): go("compare")

elif st.session_state.page == "current":
    st.markdown('<div class="title">Performance</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Current Output</div>', unsafe_allow_html=True)
    st.write("Current Energy: 520 kW")
    st.write("Production: 1800 kWh")
    st.write("Efficiency: 94%")
    st.line_chart([320,390,430,510,550,500,470])

elif st.session_state.page == "profits":
    st.markdown('<div class="title">Profits / Losses</div>', unsafe_allow_html=True)
    a,b,c=st.columns(3)
    a.metric("Revenue","$12,400")
    b.metric("Profits","$8,100")
    c.metric("Losses","$1,240")

elif st.session_state.page == "reports":
    st.markdown('<div class="title">Reports</div>', unsafe_allow_html=True)
    st.button("Daily", key="r1")
    st.button("Weekly", key="r2")
    st.button("Monthly", key="r3")
    st.download_button("PDF Download","Report","report.pdf")

elif st.session_state.page == "compare":
    st.markdown('<div class="title">Comparison</div>', unsafe_allow_html=True)
    st.line_chart({"Actual":[420,510,490],"Expected":[450,520,505]})

# ---------------- EXPECTED ----------------
elif st.session_state.page == "expected":
    st.markdown('<div class="title">Expected Data</div>', unsafe_allow_html=True)
    if st.button("Weather", key="e1"): go("weather")
    if st.button("Predictive Maintenance", key="e2"): go("maint")
    if st.button("Expected Energy Production", key="e3"): go("energy")
    if st.button("Best Time for Operation", key="e4"): go("best")
    if st.button("Recommendations + Alerts", key="e5"): go("recommend")

elif st.session_state.page == "weather":
    st.markdown('<div class="title">Weather</div>', unsafe_allow_html=True)
    a,b,c,d,e=st.columns(5)
    a.metric("Temp","34°C")
    b.metric("Humidity","48%")
    c.metric("Cloud","15%")
    d.metric("Wind","9 km/h")
    e.metric("Irradiation","920 W/m²")

elif st.session_state.page == "maint":
    st.markdown('<div class="title">Predictive Maintenance</div>', unsafe_allow_html=True)
    st.file_uploader("Upload Panel Image")
    st.info("Dust detected. Cleaning recommended.")

elif st.session_state.page == "energy":
    st.markdown('<div class="title">Expected Energy Production</div>', unsafe_allow_html=True)
    st.metric("Predicted Output","2100 kWh")

elif st.session_state.page == "best":
    st.markdown('<div class="title">Best Time for Operation</div>', unsafe_allow_html=True)
    st.success("11:00 AM - 2:00 PM")

elif st.session_state.page == "recommend":
    st.markdown('<div class="title">Recommendations + Alerts</div>', unsafe_allow_html=True)
    st.warning("Clean panels this week.")
    st.success("Battery charging optimized.")

# ---------------- BATTERY ----------------
elif st.session_state.page == "battery":
    st.markdown('<div class="title">Battery Status</div>', unsafe_allow_html=True)
    if st.button("Energy Inventory", key="b1"): go("inventory")
    if st.button("Electrical Metrics", key="b2"): go("metrics")

elif st.session_state.page == "inventory":
    st.markdown('<div class="title">Energy Inventory</div>', unsafe_allow_html=True)
    st.metric("Stored Energy","82%")
    st.metric("Available Capacity","18%")

elif st.session_state.page == "metrics":
    st.markdown('<div class="title">Electrical Metrics</div>', unsafe_allow_html=True)
    a,b,c=st.columns(3)
    a.metric("Voltage","412 V")
    b.metric("Current","32 A")
    c.metric("Temp","31°C")

# ---------------- BACK ----------------
if st.session_state.page != "home":
    st.write("")
    if st.button("← Back to Home", key="back"):
        go("home")
