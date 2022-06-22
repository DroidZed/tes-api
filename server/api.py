from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["Root"])
async def index():
  return {"message": "Unofficial The Elder Scrolls database for my discord bot"}
