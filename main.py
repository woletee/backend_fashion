from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
import models
import discover

app = FastAPI()

# ✅ Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ✅ Allow any frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Create DB tables if not present
Base.metadata.create_all(bind=engine)

# ✅ Serve uploaded images
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# ✅ Register routers
app.include_router(discover.router)
