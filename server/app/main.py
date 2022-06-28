from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from server.app.routers import spacy_ner

app = FastAPI()


# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(spacy_ner.router)
