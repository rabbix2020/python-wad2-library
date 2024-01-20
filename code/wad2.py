from wad2_entry import wad2_entry
from wad2_header import wad2_header

import struct

class wad2:
      def __init__(self):
         '''
         entries is dictionary
         where key is name of entry
         and value is entry itself

         header it's just wad2_header
         '''

         self.header = None
         self.entries = None

      def read(self, data):
         '''
         This fuction returns data
         from wad2 file.
         But, you need read full wad2 file
         and give result of this

         example:
         file = open(filename, "rb")
         self.data = file.read()
         file.close()

         file = wad2.read(data)
         '''

         file = wad2()
         file.header = wad2_header.read(data)
         self.data = data
         
         file.entries = dict()

         for index in range(file.header.numentries):
            entry = wad2_entry.read(data, file.header.diroffset, 32 * index)
            file.entries[entry.name] = entry

         return file

      def read_texture(self, data, entry: wad2_entry, texture_size: int):
          '''
          you need wad2 entry and texture size (width*height-1)
          then you will get 1D array with values that point to
          color in palette
          '''

          if not entry.type == "D":
            raise Exception("Sorry, now supports only mip textures")

          texture = [None] * texture_size
          texture_data = data[entry.offset:entry.offset+entry.dsize]
          texture_data = texture_data[::-1]
          
          for pixel in range(texture_size):
             texture[pixel] = int().from_bytes(struct.unpack("c", texture_data[pixel:pixel+1])[0])

          return texture
