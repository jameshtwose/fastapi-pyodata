from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


app = FastAPI(
    title="odata-API",
    version="0.0.1",
    description="odata API",
    contact={
        "name": "James Twose",
        "url": "https://services.jms.rocks",
        "email": "contact@jamestwose.com",
    }
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

# pass a 
@app.post("/odata")
async def odata(body: dict):
    return body

if __name__ == "__main__":
    uvicorn.run("api:app", port=8080, reload=True)