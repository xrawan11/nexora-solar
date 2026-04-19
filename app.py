import streamlit as st

st.set_page_config(page_title="Nexora Solar", layout="wide")

# ---------- STATE ----------
if "page" not in st.session_state:
    st.session_state.page = "home"

def go(page):
    st.session_state.page = page

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
font-size:42px;
font-weight:900;
font-style:italic;
color:white;
letter-spacing:2px;
}
.sun{
color:#f6b73c;
text-shadow:0 0 18px rgba(246,183,60,.55);
}

.hero{text-align:center;padding-top:60px;padding-bottom:35px;}
.hero h1{font-size:74px;font-weight:900;line-height:1.08;}
.gold{color:#f6b73c;}

.desc{
max-width:950px;
margin:auto;
font-size:20px;
line-height:1.7;
color:#d5d5d5;
}

.glow{
animation:pulse 2s infinite;
}
@keyframes pulse{
50%{box-shadow:0 0 18px rgba(246,183,60,.45);}
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
min-height:330px;
transition:.25s;
}
.mainbox:hover{
transform:translateY(-8px);
border-color:#f6b73c;
}

.mainbox h3{
font-size:28px;
color:#f6b73c;
margin-bottom:18px;
}

.subbtn{
margin-bottom:10px;
}

.title{
font-size:48px;
font-weight:900;
color:#f6b73c;
margin-top:30px;
margin-bottom:25px;
}

.subtitle{
font-size:28px;
font-weight:800;
margin-top:25px;
margin-bottom:12px;
}
</style>
""", unsafe_allow_html=True)

# ---------- TOP ----------
a,b=st.columns([8,1])
with a:
    st.markdown('<div class="logo">NEX<span class="sun">O</span>RA</div>', unsafe_allow_html=True)

with b:
    with st.popover("☰"):
        if st.button("Current Performance"): go("current")
        if st.button("AI Insights"): go("ai")
        if st.button("Expected Data"): go("expected")
        if st.button("Recommendations + Alerts"): go("recommend")
        if st.button("Battery Status"): go("battery")

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

    if st.button("Let's Start Today →"):
        go("performance")
        st.rerun()

    st.write("")

    s1,s2,s3,s4=st.columns(4)
    vals=[("15K+","Installations"),("98+","Projects Completed"),("40%","Avg. Cost Saving"),("12","Years Experience")]
    for col,(n,t) in zip([s1,s2,s3,s4],vals):
        with col:
            st.markdown(f'<div class="stat"><h2>{n}</h2><p>{t}</p></div>', unsafe_allow_html=True)

    st.write("")
    st.write("")

    c1,c2,c3=st.columns(3)

    with c1:
        st.markdown('<div class="mainbox"><h3>Performance</h3></div>', unsafe_allow_html=True)
        if st.button("Current Performance", key="p1"): go("current")
        if st.button("Profits / Losses", key="p2"): go("profits")
        if st.button("Reports", key="p3"): go("reports")
        if st.button("Comparison", key="p4"): go("compare")

    with c2:
        st.markdown('<div class="mainbox"><h3>Expected Data</h3></div>', unsafe_allow_html=True)
        if st.button("Weather", key="e1"): go("weather")
        if st.button("Predictive Maintenance", key="e2"): go("maint")
        if st.button("Expected Energy Production", key="e3"): go("energy")
        if st.button("Best Time for Operation", key="e4"): go("best")
        if st.button("Recommendations + Alerts", key="e5"): go("recommend")

    with c3:
        st.markdown('<div class="mainbox"><h3>Battery Status</h3></div>', unsafe_allow_html=True)
        if st.button("Energy Inventory", key="b1"): go("inventory")
        if st.button("Electrical Metrics", key="b2"): go("metrics")
        if st.button("Battery Status", key="b3"): go("battery")

# ---------- PERFORMANCE ----------
elif st.session_state.page == "performance":
    st.markdown('<div class="title">Performance</div>', unsafe_allow_html=True)
    st.write("Choose section from home cards.")

elif st.session_state.page == "current":
    st.markdown('<div class="title">Current Performance</div>', unsafe_allow_html=True)
    st.metric("Current Output","520 kW")
    st.metric("Production","1800 kWh")
    st.metric("Efficiency","94%")
    st.write("System Status: Normal")
    st.line_chart([320,380,430,500,540,510,470,420])

elif st.session_state.page == "profits":
    st.markdown('<div class="title">Profits / Losses</div>', unsafe_allow_html=True)
    a,b,c=st.columns(3)
    a.metric("Revenue","$12,400")
    b.metric("Profits","$8,100")
    c.metric("Losses","$1,240")
    st.bar_chart([4,6,8,7,9,12])

elif st.session_state.page == "reports":
    st.markdown('<div class="title">Reports</div>', unsafe_allow_html=True)
    st.button("Daily")
    st.button("Weekly")
    st.button("Monthly")
    st.download_button("PDF Download","Report","report.pdf")

elif st.session_state.page == "compare":
    st.markdown('<div class="title">Performance Comparison</div>', unsafe_allow_html=True)
    st.write("Actual Power vs Expected Power")
    st.line_chart({"Actual":[420,510,490],"Expected":[450,520,505]})

# ---------- EXPECTED ----------
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
    st.info("Light dust detected. Cleaning recommended.")

elif st.session_state.page == "energy":
    st.markdown('<div class="title">Expected Energy Production</div>', unsafe_allow_html=True)
    st.metric("Predicted Output","2100 kWh")

elif st.session_state.page == "best":
    st.markdown('<div class="title">Best Time for Operation</div>', unsafe_allow_html=True)
    st.success("Best operating window: 11:00 AM - 2:00 PM")

elif st.session_state.page == "recommend":
    st.markdown('<div class="title">Recommendations + Alerts</div>', unsafe_allow_html=True)
    st.warning("Clean panels this week.")
    st.success("Battery charging optimized for tomorrow.")

# ---------- BATTERY ----------
elif st.session_state.page == "inventory":
    st.markdown('<div class="title">Energy Inventory</div>', unsafe_allow_html=True)
    st.metric("Stored Energy","82%")

elif st.session_state.page == "metrics":
    st.markdown('<div class="title">Electrical Metrics</div>', unsafe_allow_html=True)
    a,b,c=st.columns(3)
    a.metric("Voltage","412 V")
    b.metric("Current","32 A")
    c.metric("Temp","31°C")

elif st.session_state.page == "battery":
    st.markdown('<div class="title">Battery Status</div>', unsafe_allow_html=True)
    a,b,c=st.columns(3)
    a.metric("Health","Healthy")
    b.metric("Cycles","1240")
    c.metric("Life Span","8.4 Years")

# ---------- BACK ----------
st.write("")
if st.button("← Home"):
    go("home")
    st.rerun()
