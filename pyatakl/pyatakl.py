# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import requests
import json
import random

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

ranpark = random.randint(0, atlen)

# <codecell>


# <codecell>

testpark

# <codecell>

class parks(object):
    def getparks(self):
        return atres
    
    def items(self):
        return atres[0]
    
    def ranpark(self):
        return atres[ranpark]

# <codecell>

#mything = parks()

# <codecell>

#for a in mything.getparks():
 #   print a

# <codecell>

test = parks()

# <codecell>

#blen = atres[0:atlen]

# <codecell>

ranitem = test.ranpark()

# <codecell>

thekeys = ranitem.keys()

# <codecell>

thekeys

# <codecell>

for kez in thekeys:
    print kez

# <codecell>

#dait = atdict.items()

# <codecell>

#atdict.viewkeys()

# <codecell>

#atrespon = atdict['response']

# <codecell>


# <codecell>

#savdict = open('/home/wcmckee/pyatakl/tests/presets/carparks.json', 'w')
#savdict.write(str(atdict))

# <codecell>

#dait

# <codecell>


# <codecell>

#atdict.values()

# <codecell>

#for d in blen:
#    print d['address']

# <codecell>

#print atext

# <codecell>


# <codecell>

#atke

# <codecell>

#atkey.name

# <codecell>


