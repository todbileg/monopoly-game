from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

FRONTEND_URL = "placeholder"
app = FastAPI()

# --- CORS SETTINGS ---
origins = [
    FRONTEND_URL, "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Monopoly Backend Online on Linux Mint!"}

@app.get("/roll-dice")
def roll_dice():
    import random
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return {
        "roll": die1 + die2,
        "detail": [die1, die2],
        "message": f"Linux Backend says: You rolled {die1 + die2}!"
    }