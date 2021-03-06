# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from flask import Flask, FlatPages
import FlatPages

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)

@app.route('/')
def index():
    return "Hello World"

@app.route('/<path:path>/')
def page(path):
    return pages.get_or_404(path).html

if __name__ == '__main__':
    app.run(port=8000)

# <codecell>


