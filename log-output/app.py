import asyncio
import uuid
from datetime import datetime, UTC
from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

app = FastAPI()
random_string = str(uuid.uuid4())  # Generated on startup

@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"Application started with ID: {random_string}")
    # Start background task for logging
    task = asyncio.create_task(log_loop())
    yield
    # Shutdown: cancel the background task
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        pass

app = FastAPI(lifespan=lifespan)

async def log_loop():
    while True:
        timestamp = datetime.now(UTC).isoformat() + "Z"
        print(f"{timestamp}: {random_string}", flush=True)
        await asyncio.sleep(5)

@app.get("/status")
async def get_status():
    timestamp = datetime.now(UTC).isoformat() + "Z"
    return {"timestamp": timestamp, "random_string": random_string}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
