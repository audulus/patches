#!/usr/bin/env python

import json
import os

print "Updating modules.md"

f = open('modules.md', 'w')

def get_description(path):
  j=json.load(open(path))

  name = os.path.splitext(os.path.split(path)[1])[0]
  png = os.path.splitext(path)[0] + ".png"

  f.write("## " + name + "\n")

  url = "./img/" + png
  url = url.replace(" ", "%20")

  f.write("![" + name + "](" + url + ")\n\n")

  if "description" in j:
     f.write(j["description"].encode('utf8'))

  f.write("\n\n")

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("."):

    for file in files:
      name, ext = os.path.splitext(file)
      if ext == ".audulus":
        get_description(root + '/' + file)


print "done!"
