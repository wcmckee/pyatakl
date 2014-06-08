# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import praw

# <codecell>

r = praw.Reddit(user_agent='redditgetsdrawn blog post')

# <codecell>

subs = r.get_subreddit('redditgetsdrawn').get_new(limit=5)

# <codecell>

[str(x) for x in subs]

# <codecell>

subs

# <codecell>

for dat in subs:
    print dat

# <codecell>

rd = r.get_subreddit('redditgetsdrawn')

# <codecell>

rd

# <codecell>

rd.description

# <codecell>

rd.fullname

# <codecell>

rd.url

# <codecell>

rd.created

# <codecell>

rd.subscribers

# <codecell>

contrrgd = rd.get_contributors()

# <codecell>

rgdh = rd.header_img

# <codecell>

rd.subreddit_type

# <codecell>

styshet = str(rd.get_stylesheet())

# <codecell>

savsty = open('style.css', 'w')

# <codecell>

savsty.write(styshet)
savsty.close()

# <codecell>

opshet = open('style.css', 'r')

# <codecell>

import json

# <codecell>

json.load(stysavz)

# <codecell>

stysavz = opshet.read()

# <codecell>


# <codecell>

rd.public_traffic

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


# <codecell>

for comes in seclis:
    print (comes)

# <codecell>

comlis = list(rd.get_comments[0])

# <codecell>

print said

# <codecell>

said = str(comlis.id)

# <codecell>

allcom = r.get_subreddit('redditgetsdrawn')

# <codecell>

suncomm = allcom.get_comments()

# <codecell>

suncomm

# <codecell>

savred = comlis.author

# <codecell>

comus = str(savred.name)

# <codecell>

lisbox = comlis.body

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

import urllib
resource = urllib.urlopen(rdgimg)
output = open(finz,"wb")
output.write(resource.read())
output.close()

# <codecell>


# <codecell>

dizusr = Image(filename=finz)

# <codecell>

dizusr

# <codecell>

url = r.get_authorize_url('uniqueKey', 'identity', True)

# <codecell>

r.login('snatchrgd', 'camp123')

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


