from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import database  # This is the database.py file you created

app = FastAPI()

# Allow Frontend (Port 3000) to talk to Backend (Port 8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Function to get a database connection for each request
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/log")
def log_activity(type: str, value: int, db: Session = Depends(get_db)):
    # 1. Calculate the points
    points_earned = value * 10
    
    # 2. Create a new "Activity" row for the database
    new_entry = database.Activity(type=type, value=value, points=points_earned)
    
    # 3. Save it to PostgreSQL
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    
    return {"status": "saved", "points_earned": points_earned, "id": new_entry.id}

@app.get("/history")
def get_history(db: Session = Depends(get_db)):
    # This pulls every log from the database to show on a leaderboard later
    return db.query(database.Activity).all()