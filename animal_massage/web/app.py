import uvicorn
from fastapi import FastAPI

from animal_massage.services import LoginInput, LoginService

app = FastAPI()


@app.post("/login")
def login(login_param: LoginInput):
    # 需要支援google、FB、Line、手機登入、一般登入
    return LoginService(login_param).login()


@app.get('/')
async def hello_world():
    return "Hello World!"


if __name__ == '__main__':
    uvicorn.run("animal_massage.web.app:app", host="0.0.0.0", port=8080, reload=True)
