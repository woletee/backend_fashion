from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
import models
import discover
import outfit  # ✅ import the outfit router
import os

app = FastAPI()

# ✅ CORS setup to allow any frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Auto-create DB tables
Base.metadata.create_all(bind=engine)

# ✅ Serve uploaded files
if not os.path.exists("uploads"):
    os.makedirs("uploads")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# ✅ Register routers
app.include_router(discover.router)
app.include_router(outfit.router)  # ✅ register outfit endpoint

# ✅ Health check
@app.get("/ping")
def ping():
    return {"message": "pong"}
