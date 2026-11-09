from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI(
    title="NEXUS API",
    description="Backend central del asistente personal NEXUS",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "name": "NEXUS",
        "message": "NEXUS is online",
        "version": "0.1.0",
    }


@app.get("/health")
async def health():
    return {
        "status": "online",
        "service": "NEXUS API",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
