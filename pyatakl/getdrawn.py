# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Get Drawn
# 
# A python script for reddit 

# <codecell>

import praw

# <codecell>

r = praw.Reddit(user_agent='redditgetsdrawn blog post')

# <codecell>

rd = r.get_subreddit('redditgetsdrawn')

# <codecell>

rd.url

# <codecell>

rd.created

# <codecell>

rd.subscribers

# <codecell>

contrrgd = rd.get_contributors()

# <codecell>


# <codecell>


# <codecell>

rgdh = rd.header_img

# <codecell>

rd.subreddit_type

# <codecell>

rd.header_title

# <codecell>

str(rd.get_random_submission())

# <codecell>

wikipg = list(rd.get_wiki_pages())[4]

# <codecell>

wikipg.has_fetched

# <codecell>

wikipg.revision_by

# <codecell>

#wikipg.content_html

# <codecell>

wikipg.content_md

# <codecell>

allmods = list(rd.get_moderators())

# <codecell>

allmods.sort()

# <codecell>

modzro = allmods[0]

# <codecell>

modcom = modzro.get_comments()

# <codecell>

for infz in modcom:
    print infz

# <codecell>

modzro.fullname

# <codecell>

print infz.subreddit

# <codecell>

print infz.body

# <codecell>

rd.get_rising

# <codecell>

rd.get_top_from_year

# <codecell>

rd.get_stylesheet()

# <codecell>

seclis = list(rd.get_comments())

# <codecell>

newcoms = []

# <codecell>

for comes in seclis:
    print (comes)
    newcoms.append(comes)

# <codecell>

senrgd = []

# <codecell>

for comz in newcoms:
    print comz
    senrgd.append(comz.submission.url)

# <codecell>

import pyimgur

# <codecell>

pyimgur.Imgur.upload_image

# <codecell>

comz.submission.url

# <codecell>

allcom = r.get_subreddit('redditgetsdrawn')

# <codecell>


# <codecell>

import bs4

# <codecell>

soup = bs4.BeautifulSoup(lisbox)

# <codecell>

soup.contents

# <codecell>

soup.index

# <codecell>

print soup.name
print soup.contents

# <codecell>

import re

myString = str(soup.string)

rdgimg = re.search("(?P<url>https?://[^\s]+)", myString).group("url")

# <codecell>

from IPython.display import Image

# <codecell>

print rdgimg

# <codecell>

import os

# <codecell>

os.chdir('/home/wcmckee/rgd')

# <codecell>

import requests

# <codecell>

reqrgd = requests.get(rdgimg)

# <codecell>

#reqrgd.text

# <codecell>

finz = (comus + '.jpg')

# <codecell>

savrgd = open(finz, 'wb')

# <codecell>

savrgd.write(reqrgd.url)
savrgd.close()

# <codecell>

finz

# <codecell>

import urllib
resource = urllib.urlopen(rdgimg)
output = open(finz,"wb")
output.write(resource.read())
output.close()

# <codecell>

ls

# <codecell>

dizusr = Image(filename=finz)

# <codecell>


# <codecell>

dizusr

# <codecell>

#r.login('snatchrgd', 'camp123')
r.login('artcontrol', 'test123')

# <codecell>

r.client_id

# <codecell>

redfront = r.get_front_page()

# <codecell>

for red in redfront:
    print red

# <codecell>

red

# <codecell>

red.comments

# <codecell>

red.downs

# <codecell>

red.title

# <codecell>

mymod = r.get_my_moderation()

# <codecell>

for mo in mymod:
    print mo

# <codecell>

rdrawn = r.get_subreddit('redditgetsdrawn')

# <codecell>

rdrawn.subscribe()

# <codecell>

rdnew = rdrawn.get_new

# <codecell>

redls = []

# <codecell>

for rd in rdnew():
    print rd
    redls.append(rd)

# <codecell>

    rd.selftext

# <codecell>

rdurlz = []
rdusers = []

# <codecell>

for itez in redls:
    print itez.url
    rdurlz.append(itez.url)
    rdusers.append(itez.author)

# <codecell>

uzrlaz = []

# <codecell>

rgdict = {'user': 'wcmckee', 'img': 'test'}

# <codecell>

for rduzr in rdusers:
    print rduzr
    uzrlaz.append(str(rduzr))
    rgdict.update({str(rduzr): 'url'})

    

# <codecell>

    rgdict

# <codecell>

for rez in uzrlaz:
    rgdict.update({'user': rez})

# <codecell>

    rgdict

# <codecell>

rgdict.update({'id': rez})

# <codecell>

rgdict

# <codecell>

uzrlaz

# <codecell>

rd.downs
rd.ups

# <codecell>

nezlis = []

# <codecell>

#rdurlz

for jpgz in rdurlz:
    if  '.jpg' in jpgz:
        nezlis.append(jpgz)
    #else print 'didnt append'
        

#if  '*.jpg' in rdurlz:
#    print '*.jpg'

# <codecell>

nezlis

# <codecell>

import random

# <codecell>

lrdz = len(rdurlz)

# <codecell>

recrand = random.randint(0, lrdz)

# <codecell>

recrand

# <codecell>

freimg = nezlis[recrand]

# <codecell>

strfre = str(freimg)

# <codecell>


# <codecell>

Image(strfre)

# <codecell>


#resource = urllib.urlopen(rdgimg)
#output = open(fulzname,"w")
#output.write(rdgimg)
#output.close()

# <codecell>

import o

# <codecell>

fulzname

# <codecell>

rdurlz

# <codecell>

savreq = requests.get(rdurlz[7])

# <codecell>

rezlz =  redls[0]

# <codecell>

reuzrz = rezlz.author

# <codecell>

usrzname = str(reuzrz.name)

# <codecell>

fulzname = (usrzname + '.jpg')

# <codecell>

resource = urllib.urlopen(rdgimg)
output = open(fulzname,"w")
output.write(rdgimg)
output.close()

# <codecell>

fulzname

# <codecell>

Image(fulzname)

# <codecell>

ls

# <codecell>

rgdtit = rd.title

# <codecell>

rdurlz = str(rd.url)

# <codecell>

rdauth =rd.author

# <codecell>

rdusern = str(rdauth.name)

# <codecell>

rdauth.is_gold

# <codecell>

rdauth.json_dict

# <codecell>

rdauth.id

# <codecell>

rdsub = rdauth.get_submitted

# <codecell>

for rsu in rdsub():
    print rsu

# <codecell>

rsu.selftext

# <codecell>

othasub = rsu.subreddit

# <codecell>

print othasub

# <codecell>

artget = r.get_subreddit('artcontroldrawsyou')

# <codecell>

artget.submit(rdusern, rdurlz )

# <codecell>

artctrl = r.get_redditor('artcontrol')

# <codecell>

arlik = artctrl.get_liked

# <codecell>

arlik

# <codecell>

print arlik

# <codecell>

print arlik()

# <codecell>


# <codecell>


