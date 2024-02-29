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

file = wad2_file.read(data)

victim = file.entries["z_exit"]
print(file.read_texture(victim))