from wad2 import wad2_file
import struct
import sys

## get WAD2 file from arguments

filename = ""
if len(sys.argv) > 1:	filename = sys.argv[1]

file = open(filename, "rb")
data = file.read()
file.close()

## The WAD2 file

file = wad2_file()
file = file.read(data)

for entry in list(file.entries):
   print(f"{entry}: {file.entries[entry].type}")