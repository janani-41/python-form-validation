from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory "database"
users = {}

@app.get("/")
def root():
    return {"message": "Login/Signup Backend running!"}

@app.post("/signup/{username}/{password}")
def signup(username: str, password: str):
    if username in users:
        return {"error": "User already exists"}
    users[username] = password
    return {"message": f"User {username} signed up successfully!"}

@app.post("/login/{username}/{password}")
def login(username: str, password: str):
    if username not in users:
        return {"error": "User not found"}
    if users[username] != password:
        return {"error": "Incorrect password"}
    return {"message": f"Welcome {username}!"}

