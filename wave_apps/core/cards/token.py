from typing import List
import requests
from h2o_wave import Q, ui
from h2o_wave.ui import Command

from .base import BaseCard
from ..utils import defaults


class TokenAttributesCard(BaseCard):
    """
    Card for handling table of token attributes.
    """
    def __init__(
        self,
        name: str = 'token_attributes',
        box: str = 'token_attributes',
        doc = None,
        # doc: Doc = None,
        token_attributes: List[str] = None,
        title: str = 'Token Attributes',
        commands: List[Command] = None
    ):
        """
        Class initialization.

        Args:
            name: Name of card
            box: Box of card
            doc: spaCy's Doc object of text
            token_attributes: Token attributes
            title: Title of card
            commands: Commands of card
        """
        super().__init__(name, box)

        self.doc = doc
        self.token_attributes = token_attributes if token_attributes is not None else defaults.TOKEN_ATTRIBUTES
        self.title = title
        print("tit title le eefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", title)
        self.commands = commands


    def get_wave_table_columns(self):
        """
        Get columns for attributes table.

        Returns:
            list: List of Wave table columns
        """
        names = {
            'i': 'id',
            'text': 'token',
            'lemma_': 'lemma',
            'norm_': 'norm',
            'ent_type_': 'ent',
            'ent_iob_': 'iob',
            'pos_': 'pos',
            'tag_': 'tag',
            'dep_': 'dep',
            'is_alpha': 'alpha',
            'is_ascii': 'ascii',
            'is_digit': 'digit',
            'is_lower': 'lower',
            'is_upper': 'upper',
            'is_title': 'title',
            'is_punct': 'punct',
            'morph': 'morph'
        }
        searchables = ['text', 'lemma', 'norm']
        filterables = self.token_attributes
        min_widths = {
            'i': '40px',
            'text': '80px',
            'lemma_': '80px',
            'norm_': '80px',
            'ent_type_': '50px',
            'ent_iob_': '40px',
            'pos_': '50px',
            'tag_': '50px',
            'dep_': '70px',
            'is_alpha': '60px',
            'is_ascii': '50px',
            'is_digit': '50px',
            'is_lower': '60px',
            'is_upper': '60px',
            'is_title': '50px',
            'is_punct': '60px',
            'morph': '70px',
        }

        return [ui.table_column(
            name=names[x],
            label=names[x],
            sortable=False,
            searchable=True if x in searchables else False,
            filterable=True if x in filterables else False,
            link=False,
            min_width=min_widths[x] if x in min_widths.keys() else None
        ) for x in self.token_attributes]

    def get_wave_table_rows(self):
        """
        Get rows for attributes table.

        Returns:
            list: List of Wave table rows
        """
        print("self.doc ", self.doc)
        # for i, token in enumerate(self.doc["result"][0]["ents"]):

        if 'detail' in self.doc or len(self.doc["result"][0]["text"]) == 0:
            return []

            # print()
            # print()
        for i, token in enumerate(self.doc["result"][0]["ents"]):
            for attr in self.token_attributes:
                print(attr, token[attr])
                # print(self.doc["result"][i]["ents"])
                # print(self.doc["result"][i]["ents"][0])
                # token = self.doc["result"][i]["ents"]
                # print("token, attr ", self.doc["result"][i][attr],"  ", attr)
        #     print()SS
        #     print()
        # # return []
        # for val in self.doc["result"][0]["ents"]:
        #     for attr in self.token_attributes:
        #         str(getattr(str(attr), str(val)))

        return [ui.table_row(
            name=str(i),
            cells=[str((token[attr]))for attr in self.token_attributes]
        )  for i, token in enumerate(self.doc["result"][0]["ents"]) ]

    async def render(self, q: Q):
        """
        Render card in Wave.

        Args:
            q: Wave server

        """
        url = "http://127.0.0.1:8000/process/?model=en_core_web_sm"
        headers = {'Content-type': 'application/json', 'accept': 'application/json'}

        data = '[ {' + f'"text": "{q.client.input_text}"' + ' } ]'

        print("q.client.input_text ", q.client.input_text)
        # print("q.client.input_text 1", q.client.input_text_1)
        # print("q.client.input_text 2", q.client.input_text_2)
        self.doc = requests.post(url, data=data, headers=headers).json()
        print(self.doc["result"][0]["ents"])
        card = ui.form_card(
            box=self.box,
            items=[
                ui.table(
                    name='table_tokens',
                    columns=self.get_wave_table_columns(),
                    rows=self.get_wave_table_rows(),
                    downloadable=True,
                    resettable=True
                )
            ],
            title=self.title,
            commands=self.commands
        )

        q.page[self.name] = card
