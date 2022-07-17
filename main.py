from fastapi import FastAPI

from services import create_link_token, retrieve_account_token

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://localhost:63342",  # Serving HTML file from PyCharm
    "http://127.0.0.1:5500"  # Serving HTML file from VS Code
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/create-link-token")
def get_link_token():
    token = create_link_token()
    return token


@app.get("/retrieve_account_token/{public_token}")
def get_account_token(public_token: str):
    print(public_token)
    account_token = retrieve_account_token(public_token)
    return account_token
