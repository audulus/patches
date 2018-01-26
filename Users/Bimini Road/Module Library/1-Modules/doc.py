#!/usr/bin/env python

import json
import os

print "Updating modules.md"

f = open('modules.md', 'w')

def get_description(path):
  j=json.load(open(path))

  name = os.path.splitext(os.path.split(path)[1])[0]

  f.write("### " + name + "\n")

  if "description" in j:
     f.write(j["description"].encode('utf8'))

  f.write("\n\n")

# traverse root directory, and list directories as dirs and files as files
dirs = next(os.walk('.'))[1]
for dir in dirs:

    f.write("## " + dir + "\n")

    for root, dirs, files in os.walk(dir):

        for file in files:
            name, ext = os.path.splitext(file)
            if ext == ".audulus":
                print root
                print file
                print os.path.split(root)
                get_description(root + '/' + file)


print "done!"
