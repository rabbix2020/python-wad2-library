from wad2 import wad2
import sys

## get WAD2 file from arguments

filename = ""
if len(sys.argv) > 1:	filename = sys.argv[1]

file = open(filename, "rb")
data = file.read()
file.close()

## The WAD2 file

file = wad2.read(data)

entries = list(file.entries.keys())

for entry_name in entries:
    print(entry_name)
