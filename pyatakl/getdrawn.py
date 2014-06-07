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

comlis

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

myString = str(soup.index)

rdgimg = re.search("(?P<url>https?://[^\s]+)", myString).group("url")

# <codecell>

from IPython.display import Image

# <codecell>

i = Image(filename=rdgimg)

# <codecell>


