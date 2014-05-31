# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import requests
import json
import random

# <markdowncell>

# <h1>Python Auckland Transport</h1> 

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
    
    def parkloc(self):
        return(atres[ranpark]['address'])
    
    def parkid(self):
        return(atres[renpark]['id'])
    
    def parkcheck():
        return(atres[renpark]['type'])
    
    def parknon(self, inpuz ):
        return(atres[renpark][inpuz])

# <codecell>


# <codecell>

park = parks()

# <codecell>

park.genpark()

# <codecell>

park.parkloc()

park.parknon()

# <codecell>

park.parkid()

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


# <codecell>

getdispl = ('http://api.at.govt.nz/v1/public/realtime/vehiclelocations?api_key=433feddb-d4b9-473b-a0c2-ac982a6d78cd')

# <codecell>

getres = requests.get(getdispl)

# <codecell>

gettx = getres.text

# <codecell>

pajson = json.loads(gettx)

# <codecell>

patza = pajson.keys()

# <codecell>

pajson.keys()

# <codecell>

for i in pajson:
    print i

# <codecell>

patze = pajson['response']['entity'][0]

# <codecell>

patze

# <codecell>

paveh = patze['vehicle']

# <codecell>

pala = paveh['position']

# <codecell>

print pala

# <codecell>

palat = pala['latitude'] 

# <codecell>

palat

# <codecell>

palong = pala['longitude']

# <codecell>

palong

# <codecell>

class busdata(object):
    
    def latdata(self):
        return palat
    def longdata(self):
        return palong
    

# <codecell>

busdata = busdata()

# <codecell>

busdata.longdata()

# <codecell>


# <codecell>

busdata.latdata()

# <codecell>


