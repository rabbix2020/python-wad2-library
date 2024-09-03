from wad2 import wad2_file
import sys

## get WAD2 file from arguments

filename = ""
if len(sys.argv) > 1:	filename = sys.argv[1]

file = open(filename, "rb")
data = file.read()
file.close()

## The WAD2 file

file = wad2_file.read(data)

victim = file.entries["IN_1"]

print(len(file.read_texture(victim)))
