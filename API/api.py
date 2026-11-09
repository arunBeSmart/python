from fastapi import FastAPI
app = FastAPI(title="My API", description="This is a sample API built with FastAPI.", version="1.0.0"
              )
@app.get("/hello")
def hello():
    return {"message": "Hello, data!"}

@app.get("/home")
def home():
    return {"message": "home"}


    
