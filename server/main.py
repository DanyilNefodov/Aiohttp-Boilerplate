# aiohttpdemo_polls/main.py
import aiohttp.web as web
import aiohttp_jinja2
import jinja2

from db import (
    close_pg,
    init_pg
)
from middlewares import (
    setup_middlewares
)
from routes import (
    setup_routes,
    setup_static_routes
)
from settings import (
    TEMPLATES_DIR
)

app = web.Application()
aiohttp_jinja2.setup(
    app,
    loader=jinja2.FileSystemLoader(
        str(TEMPLATES_DIR)
    )
)
setup_routes(app)
setup_static_routes(app)
setup_middlewares(app)
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)
web.run_app(app)
