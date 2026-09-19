from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.clans import router as clan_router

app = FastAPI(
    title="Clan Intelligence SaaS API",
    description="Backend Service for CoC Analytics & Railway Deployment",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(clan_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Clan Intelligence API Online", "docs": "/docs"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
