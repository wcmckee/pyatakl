# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

digital ocean server setup and installing ipython notebook, and run website on web server. 
choose os you want, choose images you want. launch. 

# <markdowncell>

# user logs into digital ocean, chooses one of my snapshots (need to make snapshots of stuff i like.
# Makes server, runs script to install software. tick box on software you want. 
# 

# <codecell>

from dop.client import Client

# <codecell>

client = Client()

# <codecell>

ls

# <codecell>

%%bash
ipython nbconvert 'digzocean.ipynb'

# <codecell>

cat digzocean.html

# <codecell>

import os

# <codecell>

os.chdir('/home/wcmckee/brobeur-web/')

# <codecell>

ls

# <codecell>

rm -rf imgs

# <codecell>

ls

# <codecell>


