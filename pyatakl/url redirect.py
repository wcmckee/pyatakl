# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

optxt = open('brief.txt', 'r')

# <codecell>

filtxt = optxt.read()

# <codecell>

filtxt

# <codecell>

filtxt.

# <codecell>

mksit = open('index.html', 'w')

# <codecell>


# <codecell>

import requests

# <codecell>

opartz = requests.get('http://artcontrol.me')

# <codecell>

headon = opartz.headers

# <codecell>

headon

# <codecell>

headon.keys()

# <codecell>

print headon['server']

# <codecell>

checkser = headon['server']

# <codecell>


# <codecell>

if checkser is None:
    print ('it is none')
    
else:
    print ('You have a referal header')

# <codecell>


