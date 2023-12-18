# main.py
from fastapi import FastAPI, Request
from database import set_user_role, get_profiles

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    body = await request.json()
    user = body["user_name"]
    set_user_role(user)
    response = await call_next(request)
    return response


@app.post("/profiles")
async def read_root():
    profiles = get_profiles()
    return profiles


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
