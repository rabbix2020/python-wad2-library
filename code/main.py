from wad2 import wad2
import sys

## get WAD2 file from arguments

filename = ""
if len(sys.argv) > 1:	filename = sys.argv[1]

file = open(filename, "rb")
data = file.read()
file.close()

## The WAD2 file

file = wad2()
file = file.read(data)

for entry_name in file.entries:
    entry = file.entries[entry_name]

victim = entry
texture_data = file.read_texture(data=data, entry=victim, texture_size=16*16-1)
print(texture_data[0])
