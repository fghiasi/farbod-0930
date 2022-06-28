from pydantic import BaseModel
from typing import List

from .article import Article
from .model_name import ModelName

DEFAULT_MODEL = ModelName.en_core_web_sm


class RequestModel(BaseModel):

    articles: List[Article]
    model: ModelName = DEFAULT_MODEL

