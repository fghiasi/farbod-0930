from h2o_wave import ui

INPUT_MODELS = ['en_core_web_sm', 'en_core_web_md']
INPUT_MODEL = 'en_core_web_sm'
INPUT_TITLE = ''
INPUT_SUBTITLE = ''
INPUT_TEXT = ''

META_CARD = ui.meta_card(
    box='',
    title='',
    icon='',
    layouts=[
        ui.layout(
            breakpoint='xs',
            zones=[
                ui.zone(name='header'),
                ui.zone(name='main', zones=[
                    ui.zone(name='input_row', zones=[

                        ui.zone(name='input_text')
                    ]),
                    ui.zone(name='entity_row', direction='row', zones=[
                        ui.zone(name='entity_settings', size='30%'),
                        ui.zone(name='input_model'),
                        ui.zone(name='entity_visualizer', size='70%')
                    ]),
                    ui.zone(name='token_attributes')
                ]),
                ui.zone(name='footer')
            ]
        )
    ],
    themes=[
        ui.theme(
            name='h2o-dark',
            primary='#09e8c7',
            text='#e8e1e1',
            card='#0a0a30',
            page='#070b1a',
        )
    ],
    theme='h2o-dark'
)
HEADER_CARD = ui.header_card(
    box='header',
    title='Service and UI to Showcase Named Entity Recognition.',
    subtitle=''
)

FOOTER_CARD = ui.footer_card(
    box='footer',
    caption='(c) 2022 <b>Institutional Shareholder Services is the world\'s leading provider of corporate governance and responsible investment solutions.</b> - <i>Junior SRE, Machine Learning and Data Infrastructure Project.</i>'
)

TOKEN_ATTRIBUTES = ['i', 'text', 'lemma_', 'norm_', 'ent_type_', 'ent_iob_', 'pos_', 'tag_', 'dep_', 'is_alpha',
                    'is_ascii', 'is_digit', 'is_lower', 'is_upper', 'is_title', 'is_punct', 'morph']
