from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import company, job
from database import Base, engine
from models import company as company_model, job as job_model

app = FastAPI()

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],      # Allow all HTTP methods
    allow_headers=["*"],      # Allow all headers
)

# Create database tables
# Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(company.router)
app.include_router(job.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/about")
def read_about():
    return {"about": "This is about page"}


@app.get("/contact")
def read_contact():
    return {"contact": "This is contact page"}