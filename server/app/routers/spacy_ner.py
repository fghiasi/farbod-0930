import spacy
from fastapi import APIRouter, Depends

from server.app.apis.spacy_ner.response_model import ResponseModel
from server.app.apis.spacy_ner.request_model import RequestModel
from server.app.apis.spacy_ner.model_name import ModelName
from server.app.apis.spacy_ner.get_data import get_data


MODEL_NAMES = [model.value for model in ModelName]
MODELS = {name: spacy.load(name) for name in MODEL_NAMES}

router = APIRouter()


@router.post("/process/", summary="Process batches of text", response_model=ResponseModel, tags=["NER Process"])
async def process_articles(query: RequestModel = Depends(RequestModel)):
    """Process a batch of articles and return the entities predicted by the
    given model. Each record in the data should have a key "text".
    """
    nlp = MODELS[query.model]
    response_body = []
    texts = (article.text for article in query.articles)

    for doc in nlp.pipe(texts):
        print("doc ", doc)

        response_body.append(get_data(doc))
    return {"result": response_body}
