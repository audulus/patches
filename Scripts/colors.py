#!/usr/bin/env python

# Update SVG colors in a patch.
# Instead of doing a global regex on stroke:#xxxxxx
# we traverse to find SVG nodes and then do the regex.

import json
import sys
import re

data = json.load(open(sys.argv[1]))
regex = re.compile(r"(stroke:#......)")

def updateColors(patch):

    for node in patch["nodes"]:
        if node["type"] == "Patch":
            updateColors(node["subPatch"])
        if node["type"] == "SVG":
            print regex.sub("stroke:#293e4d", node["svg"])

updateColors(data["patch"])

with open(sys.argv[1], 'w') as outfile:
    json.dump(data, outfile, separators=(',', ':'))
