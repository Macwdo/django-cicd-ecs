import asyncio
from datetime import datetime

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def health_check():
    await io_blocking_function()        
    return {"status": "ok", "time": datetime.now()}

@app.get("/async")
async def async_health_check():
    asyncio.create_task(io_blocking_function())
    return {"status": "ok", "time": datetime.now()}

async def io_blocking_function():
    await asyncio.sleep(4)
    print("IO blocking function done")