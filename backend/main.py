from fastapi import FastAPI

app = FastAPI(title="Nexora Solar API Fresh")

@app.get("/")
def home():
    return {"message":"Nexora API Running"}

@app.get("/performance")
def performance():
    return {"current_power":520,"production":1800,"efficiency":94,"status":"Excellent"}

@app.get("/battery-status")
def battery():
    return {"battery_level":82,"temperature":31,"status":"Healthy"}

@app.get("/weather")
def weather():
    return {
        "temp":34,
        "clouds":15,
        "wind_speed":9,
        "status":"Sunny"
    }

@app.get("/expected-data")
def expected():
    return {
        "predicted_output":2100,
        "tomorrow_efficiency":92,
        "maintenance_risk":"Low",
        "dust_probability":18,
        "battery_forecast":85
    }



print("Fresh API on port 8001")
