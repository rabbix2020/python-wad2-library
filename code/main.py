from wad_entry import wad_entry
from wad_header import wad_header

import sys

filename = ""
if len(sys.argv) > 1:	filename = sys.argv[1]

file = open(filename, "rb")
data = file.read()
file.close()

## The WAD2 file header

header = wad_header()

header = wad_header.read(data)

## The WAD directory

for index in range(header.numentries):
    entry = wad_entry.read(data, header.diroffset, 32 * index)
    print(f"{entry.name} type: {entry.type}")
