from fastapi import FastAPI
import tasks

app = FastAPI()

@app.get("/first_task")
def first_task():
    resp = tasks.first()
    return resp

