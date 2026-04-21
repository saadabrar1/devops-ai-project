from fastapi import FastAPI
import random
import time

app = FastAPI()

@app.get("/")
def home():
    return {"message": "DevOps + AIOps project running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    return {
        "cpu_usage": random.randint(10, 90),
        "memory_usage": random.randint(20, 80),
        "response_time": round(random.uniform(0.1, 1.5), 2)
    }
