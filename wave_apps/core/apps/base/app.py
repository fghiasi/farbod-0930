from h2o_wave import Q, ui, copy_expando
# from spacy import load as spacyload

from ...cards import (
    InputModelCard, InputTextCard,
    EntitySettingsCard,
    TokenAttributesCard,
)
from ...utils import defaults


class BaseApp:
    _META_CARD = defaults.META_CARD
    _HEADER_CARD = defaults.HEADER_CARD
    _FOOTER_CARD = defaults.FOOTER_CARD
    _INPUT_MODEL_CARD = InputModelCard()
    _INPUT_TEXT_CARD = InputTextCard()
    _ENTITY_SETTINGS_CARD = EntitySettingsCard()
    _TOKEN_ATTRIBUTES_CARD = TokenAttributesCard()

    def __init__(
        self,
        meta_card: ui.MetaCard = None,
        header_card: ui.HeaderCard = None,
        footer_card: ui.FooterCard = None,
        input_model_card: InputModelCard = None,
        input_text_card: InputTextCard = None,
        entity_settings_card: EntitySettingsCard = None,
        token_attributes_card: TokenAttributesCard = None,
    ):
        self.meta_card = meta_card if meta_card is not None else self._META_CARD
        self.header_card = header_card if header_card is not None else self._HEADER_CARD
        self.footer_card = footer_card if footer_card is not None else self._FOOTER_CARD
        self.input_model_card = input_model_card if input_model_card is not None else self._INPUT_MODEL_CARD
        self.input_text_card = input_text_card if input_text_card is not None else self._INPUT_TEXT_CARD
        self.entity_settings_card = entity_settings_card if entity_settings_card is not None else \
            self._ENTITY_SETTINGS_CARD
        self.token_attributes_card = token_attributes_card if token_attributes_card is not None else \
            self._TOKEN_ATTRIBUTES_CARD

    async def serve(self, q: Q) -> None:
        copy_expando(q.args, q.client)
        if not q.client.client_initialized:
            await self._initialize_client(q)
            q.client.client_initialized = True
        elif q.args.input_model:
            await self._load_model(q)
            await self._process_text(q)
            await self._update_all_cards(q)
        elif q.args.analyze_text:
            await self._process_text(q)
            await self._update_all_cards(q)
        elif q.args.select_ents:
            await self._update_entity_cards(q)

    async def _initialize_client(self, q: Q):
        q.client.input_models = self.input_model_card.input_models
        q.client.input_model = self.input_model_card.input_model

        await self._load_model(q)

        q.client.input_text = self.input_text_card.input_text
        q.client.input_text_1 = self.input_text_card.input_text
        q.client.input_text_2 = self.input_text_card.input_text
        print(" q.client.input_text ", q.client.input_text )
        print(" q.client.input_text_1 ", q.client.input_text_1)
        print("q.client.input_text_2 ", q.client.input_text_2)

        await self._process_text(q)

        q.page['meta'] = self.meta_card
        q.page['header'] = self.header_card
        q.page['footer'] = self.footer_card

        # print("q.client.doc.ents issssssssssss ", q.client.doc.ents)
        if q.client.doc is not None:
            q.client.select_ents = sorted(list(set([x.label_ for x in q.client.doc.ents])))

        await self._update_all_cards(q)

    @staticmethod
    async def _load_model(q: Q):
        print("async def _load_model(q: Q):")
        # q.client.model = spacyload(q.client.input_model)
        print("q.client.model = ", q.client.model)

    @staticmethod
    async def _process_text(q: Q):
        print("async def _process_text(q: Q):")
        print(".client.input_text = ", q.client.input_text)
        print("q.client.input_text_1 ", q.client.input_text_1)
        print("q.client.input_text_2 = ", q.client.input_text_2)
        # q.client.doc = q.client.model(q.client.input_text)
        # q.client.doc_1 = q.client.model(q.client.input_text_1)
        # q.client.doc_2 = q.client.model(q.client.input_text_2)
        print("q.client.doc = ", q.client.doc)
        print("q.client.doc_1  ", q.client.doc_1 )
        print("q.client.doc_2 = ", q.client.doc_2)

    async def _update_all_cards(self, q: Q):
        await self._update_input_cards(q)
        await self._update_entity_cards(q)
        await self._update_token_cards(q)

        await q.page.save()

    async def _update_input_cards(self, q: Q):
        self.input_model_card.input_model = q.client.input_model
        await self.input_model_card.render(q)

        self.input_text_card.input_text = q.client.input_text
        await self.input_text_card.render(q)

    async def _update_entity_cards(self, q: Q):
        print("async def _update_entity_cards(self, q: Q):")
        print()
        # self.entity_settings_card.choice_ents = list(q.client.model.get_pipe('ner').labels)
        print("self.entity_settings_card.choice_ents  ", self.entity_settings_card.choice_ents )
        self.entity_settings_card.select_ents = q.client.select_ents
        await self.entity_settings_card.render(q)


    async def _update_token_cards(self, q: Q):
        # print("async def _update_token_cards(self, q: Q): ")
        data = '[ { "text": "I Love USA And LA" } ]'
        # self.token_attributes_card.doc = q.client.doc
        # print("q.client.doc ", q.client.doc)
        await self.token_attributes_card.render(q)
