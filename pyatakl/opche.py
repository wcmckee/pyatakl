# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#! /usr/bin/python

import dominate # 'pip install dominate' must be run once before this
from dominate.tags import *
import re # Only needed because dominate doesn't let us set tab indentation
import tempfile
import webbrowser

# <codecell>

checkdom = dominate.tags.a('check', 'blah')

# <codecell>

checkdom()

# <codecell>


