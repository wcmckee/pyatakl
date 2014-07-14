# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

ls

# <codecell>

cd ..

# <codecell>

ls

# <codecell>

cd ..

# <codecell>

ls

# <codecell>

import subprocess

# <codecell>

cd artcontrolme/

# <codecell>

ls

# <codecell>

cd /home/wcmckee/

# <codecell>

ls

# <codecell>

cd artcontrolme/

# <codecell>

 -e robots=off --wait 0.25

# <codecell>

%%bash

wget \
     -e robots=off --wait 0.25 \
     --recursive \
     --no-clobber \
     --page-requisites \
     --html-extension \
     --convert-links \
     --restrict-file-names=windows \
     --domains centralkids.org.nz \
     --no-parent \
         http://www.centralkids.org.nz/whaihanga-early-learning-centre

# <codecell>


