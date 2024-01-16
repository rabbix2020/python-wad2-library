## check this site to understand what's going on -> https://www.gamers.org/dEngine/quake/spec/quake-spec34/qkspec_7.htm

import struct

class wad2_entry:
     def __init__(self):
        offset = 0
        dsize = 0
        size = 0
        type = 0
        cmprs = 0
        dummy = 0
        name = ""

     @staticmethod
     def read(data, diroffset, offset):
        entry = wad2_entry()
        entry.offset = struct.unpack("i", data[diroffset+offset:diroffset+offset+4])[0]
        entry.dsize = struct.unpack("i", data[diroffset+offset+4:diroffset+offset+8])[0]
        entry.size = struct.unpack("i", data[diroffset+offset+8:diroffset+offset+12])[0]
        entry.type = struct.unpack("c", data[diroffset+offset+12:diroffset+offset+13])[0].decode("ascii")
        entry.cmprs = struct.unpack("c", data[diroffset+offset+13:diroffset+offset+14])[0]
        entry.dummy = struct.unpack("h", data[diroffset+offset+14:diroffset+offset+16])[0]
        entry.name = data[diroffset+offset+16:diroffset+offset+32].decode("ascii")
        entry.name = entry.name.replace('\0', '')

        return entry