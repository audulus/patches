#!/usr/bin/env python

# Update SVG colors in a patch.

import sys
import re

s = open(sys.argv[1]).read()
regex = re.compile(r"(stroke:#......)")

# stroke:#293e4d
# stroke:#82D1E0
s = regex.sub("stroke:#82D1E0", s)
s = re.sub(r"(stroke-width:1\.5px)", "stroke-width:1px", s)
open(sys.argv[1], 'w').write(s)

