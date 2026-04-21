from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "DevOps AI App Running"}

# THIS LINE SHOULD BE PRESENT
Instrumentator().instrument(app).expose(app)
