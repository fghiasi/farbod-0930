from pydantic import BaseModel
from typing import List


class ResponseModel(BaseModel):
    # This is the schema of the expected response and depends on what you
    # return from get_data.

    class Batch(BaseModel):
        class Entity(BaseModel):
            label: str
            start: int
            end: int
            text: str

        text: str
        ents: List[Entity] = []

    result: List[Batch]
