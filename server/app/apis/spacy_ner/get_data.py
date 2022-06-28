from spacy.tokens import Doc
from typing import Dict, Any


def get_data(doc: Doc) -> Dict[str, Any]:
    """Extract the data to return from the REST API given a Doc object. Modify
    this function to include other data."""

    ents = [
        {
            "text": ent.text,
            'i': ent.i,
            'lemma_': ent.lemma_,
            'norm_': ent.norm,
            'ent_type_': str(ent),
            'ent_iob_': ent.ent_iob,
            'pos_': ent.pos_,
            'tag_': ent.tag_,
            'dep_': ent.dep_,
            'is_alpha': ent.is_alpha,
            'is_ascii': ent.is_ascii,
            'is_digit': ent.is_digit,
            'is_lower': ent.is_lower,
            'is_upper': ent.is_upper,
            'is_title': ent.is_title,
            'is_punct': ent.is_punct,
            'morph': str(ent.morph)
        }
        for ent in doc
    ]
    return {"text": doc.text, "ents": ents}
