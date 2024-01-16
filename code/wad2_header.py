## check this site to understand what's going on -> https://www.gamers.org/dEngine/quake/spec/quake-spec34/qkspec_7.htm

import struct

class wad2_header:
     def __init__(self):
       self.magic = ""
       self.numentries = 0
       self.diroffset = 0

     @staticmethod
     def read(data):
        header = wad2_header()
        header.magic = data[:4].decode("ascii")

        if not header.magic == "WAD2":
           raise TypeError("wad_header.read(): it's not a WAD2 file")

        header.numentries = struct.unpack("i", data[4:8])[0]
        header.diroffset = struct.unpack("i", data[8:12])[0]

        return header