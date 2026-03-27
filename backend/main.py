from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "EcoTrack Backend is Running!"}

@app.post("/log")
def log_activity(type: str, value: int):
    points = value * 10
    return {"type": type, "points_earned": points}