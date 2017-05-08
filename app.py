import os
import asyncio
import uvloop
from sanic import Sanic
from sanic.response import html, json
from sanic.exceptions import NotFound
from sanic_jinja2 import SanicJinja2
from db import setup_db

app = Sanic()
jinja = SanicJinja2(app)

@app.route("/")
async def root(request):
    return jinja.render('index.html', request)

@app.route("/load_info")
async def root(request):
    return json({})

@app.exception(NotFound)
def ignore_404s(request, exception):
    return jinja.render('404.html', request, url=request.url)

if __name__ == "__main__":
    setup_db()
    app.run(host="0.0.0.0", port=8000, workers=os.cpu_count())
