from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

counter = 0

@app.get("/", response_class=PlainTextResponse)
async def root():
    return "Welcome to the Ping-Pong API!"


@app.get("/pingpong", response_class=PlainTextResponse)
async def ping():
    global counter
    value = counter
    counter += 1
    return f"pong {value}"

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(8000))
