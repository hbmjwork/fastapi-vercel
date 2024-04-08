from fastapi import FastAPI, Body
from pydantic import BaseModel

class HelloWorldResponse(BaseModel):
    message: str
  
app = FastAPI()

@app.get("/", tags=["Root"])
async def hello():
  return {"message": "Hello World!"}

@app.get("/helloworld", response_model=HelloWorldResponse)
async def helloworld():
    return HelloWorldResponse(message="Hello World!")
