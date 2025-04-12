from fastapi import FastAPI

app = FastAPI()

# HTTP GET endpoint
@app.get("/")
def hello(name: str = "World"):
    return f"Hello, {name}!"