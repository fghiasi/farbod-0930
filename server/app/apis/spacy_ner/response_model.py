
from pydantic import BaseModel
from typing import List


class ResponseModel(BaseModel):
    # This is the schema of the expected response and depends on what you
    # return from get_data.

    class Batch(BaseModel):
        class Entity(BaseModel):
            text: str
            i: int
            lemma_: str
            norm_: int
            ent_type_: str
            ent_iob_: int
            pos_: str
            tag_: str
            dep_: str
            is_alpha: bool
            is_ascii: bool
            is_digit: bool
            is_lower: bool
            is_upper: bool
            is_title: bool
            is_punct: bool
            morph: str

        text: str
        ents: List[Entity] = []

    result: List[Batch]
