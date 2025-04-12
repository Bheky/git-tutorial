from fastapi import FastAPI

app = FastAPI()

# HTTP GET endpoint
@app.get("/")
def hello(name: str = "World"):
    return f"Hello, {name}!"

# Goodbye endpoint
@app.get("/goodbye")
def goodbye():
    return "Goodbye, World!"