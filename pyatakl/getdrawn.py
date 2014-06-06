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


