import os
import asyncio
import uvloop
from sanic import Sanic
from sanic.response import text, json, file
from sanic.exceptions import NotFound, RequestTimeout
from sanic_jinja2 import SanicJinja2
from jinja2 import FileSystemLoader
import db

app = Sanic()
jinja = SanicJinja2(app, loader=FileSystemLoader('./templates'))
port = int(os.environ.get('PORT', '5000'))
app.static('/static', './static')


@app.route("/")
async def root(request):
    return jinja.render('index.html', request)


@app.route("/load_info")
async def root(request):
    res = await db.get_langs_data()
    return json(res)


@app.exception(NotFound)
def not_found(request, exception):
    return text("Not found")


@app.exception(RequestTimeout)
def timeout(request, exception):
    return text("")


if __name__ == "__main__":
    db.setup_db()
    app.config.LOGO = None
    app.run(host="0.0.0.0", port=port, workers=os.cpu_count())
