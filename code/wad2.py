from wad2_entry import wad2_entry
from wad2_header import wad2_header

import mip
import palette

class wad2_file:
      def __init__(self):
         '''
         entries is dictionary
         where key is name of entry
         and value is entry itself

         header it's just wad2_header
         data it's just data of file
         '''

         self.data = None
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

         file = wad2_file()
         file.header = wad2_header.read(data)
         file.data = data
         
         file.entries = dict()

         for index in range(file.header.numentries):
            entry = wad2_entry.read(data, file.header.diroffset, 32 * index)
            file.entries[entry.name] = entry

         return file

      def read_texture(self, entry: wad2_entry) -> list:
          '''
          in case if entry is palette you will get 1D array with all colors in this palette
          in case if entry is mip texture will get dictionary with size and array with 4 other arrays where stores textures
          '''
          texture_data = self.data[entry.offset:entry.offset+entry.dsize]

          match entry.type:
               case '@':
                   return palette.read(texture_data)
               case 'D':
                   return mip.read(texture_data)
               case 'E':
                   return texture_data
               case _:
                   raise Exception("Sorry, other types if not supported now")