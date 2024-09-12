from fastapi import FastAPI

app = FastAPI()

@app.get("/hello") 
async def hello(): 
    return {"message": "world"}

@app.get("/check")
async def hi(): 
    return {"message": "Status Good!"}