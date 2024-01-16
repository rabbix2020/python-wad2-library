from wad2 import wad2

import sys

filename = ""
if len(sys.argv) > 1:	filename = sys.argv[1]

file = open(filename, "rb")
data = file.read()
file.close()

## The WAD2 file

file = wad2.read(data)

print(file.entries)