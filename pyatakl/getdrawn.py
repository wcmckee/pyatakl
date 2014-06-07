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

rd.public_traffic

# <codecell>

rd.header_title

# <codecell>


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

list(rd.get_moderators())

# <codecell>

rd.get_rising

# <codecell>

rd.get_top_from_year

# <codecell>

rd.get_stylesheet()

# <codecell>

comlis = list(rd.get_comments('all'))[0]

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

soup.

# <codecell>

import re

myString = str(soup.string)

rdgimg = re.search("(?P<url>https?://[^\s]+)", myString).group("url")

# <codecell>

from IPython.display import Image

# <codecell>

i = Image(filename=rdgimg)

# <codecell>

print rdgimg

# <codecell>

import os

# <codecell>

os.mkdir('/home/wcmckee/rgd')

# <codecell>

os.chdir('/home/wcmckee/rgd')

# <codecell>

pwd

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

import envoy

# <codecell>

r = envoy.run('wget ' + rdgimg)

# <codecell>

print r.std_out

# <codecell>

print r.status_code

# <codecell>

mwg = envoy.run('man wget')

# <codecell>

mwg.command

# <codecell>

mwg.std_out

# <codecell>


