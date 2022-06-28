from pydantic import BaseModel


class Article(BaseModel):
    # Schema for a single article in a batch of articles to process
    text: str
