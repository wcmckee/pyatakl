# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import requests
import json
import random

# <codecell>

atdat = requests.get('https://api.at.govt.nz/v1/public/display/parkinglocations?api_key=433feddb-d4b9-473b-a0c2-ac982a6d78cd')

# <codecell>

newurl = ('https://api.at.govt.nz/v1/public/realtime/vehiclelocations')

# <codecell>

agency = ('gtfs/agency')

# <codecell>

startu = ('https://api.at.govt.nz/v1/public/')

# <codecell>

mergu = startu + agency

# <codecell>

mergu

# <codecell>

adpre = (mergu + '?api_key=433feddb-d4b9-473b-a0c2-ac982a6d78cd' )

# <codecell>

atoiat = requests.get('https://api.at.govt.nz/v1/public/gtfs/agency?api_key=433feddb-d4b9-473b-a0c2-ac982a6d78cd')

# <codecell>

atbat = requests.get('https://api.at.govt.nz/v1/public/agency?api_key=433feddb-d4b9-473b-a0c2-ac982a6d78cd')

# <codecell>

atbat

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

#mything = parks()

# <codecell>

#for a in mything.getparks():
 #   print a

# <codecell>

#blen = atres[0:atlen]

# <codecell>

ranitem = test.ranpark()

# <codecell>

thekeys = ranitem.keys()

# <codecell>

thekeys

# <codecell>

listz = []

# <codecell>

for kez in thekeys:
    #print key
    print atres[0][kez]
    listz.append(atres[0][kez])
    

# <codecell>

#dait = atdict.items()

# <codecell>

print listz[3]

# <codecell>

import geopy

# <codecell>

geo = geopy.GoogleV3()

# <codecell>

geo.geocode(listz[3])

# <codecell>

olenz = len(listz)

# <codecell>

dachoice = random.randint(0, olenz)

# <codecell>

dachoice

# <codecell>

class parks(object):
    def getparks(self):
        return atres
    
    def items(self):
        return atres[0]
    
    def ranpark(self):
        return atres[ranpark]
    
    def genpark(self):
        return (geo.geocode(listz[3]))
    
    def geopark(self):
        return(geo.geocode(listz[dachoice]))
    
    

# <codecell>

test = parks()

# <codecell>

test.genpark()

# <codecell>

test.geopark()

# <codecell>

geo.geocode(listz[3])

# <codecell>

listz.sort()

# <codecell>

listz

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


