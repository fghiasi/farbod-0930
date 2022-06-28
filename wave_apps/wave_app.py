# wave_app.py
from h2o_wave import Q, main, app
from core.apps import BaseApp

core_app = BaseApp()


@app('/')
async def serve(q: Q):
    await core_app.serve(q)
