from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from server.app.routers import spacy_ner

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://127.0.0.1:8000",
    "http://localhost:8080",
]
# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(spacy_ner.router)
