# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import requests
import json

# <codecell>

atdat = requests.get('https://api.at.govt.nz/v1/public/display/parkinglocations?api_key=433feddb-d4b9-473b-a0c2-ac982a6d78cd')

# <codecell>

atext = atdat.text

# <codecell>

atdict = json.loads(atext)

# <codecell>

atres = atdict['response']

# <codecell>

atlen = len(atres)

# <codecell>

class parks:
    def getparks():
        print dait

# <codecell>

mything = parks()

# <codecell>

mything.getparks()

# <codecell>

blen = atres[0:atlen]

# <codecell>

dait = atdict.items()

# <codecell>


# <codecell>

savdict = open('/home/wcmckee/pyatakl/tests/presets/carparks.json', 'w')
savdict.write(str(atdict))

# <codecell>

dait

# <codecell>


# <codecell>

atdict.values()

# <codecell>

for d in blen:
    print d['address']

# <codecell>

print atext

# <codecell>


# <codecell>

atke

# <codecell>

atkey.name

# <codecell>


