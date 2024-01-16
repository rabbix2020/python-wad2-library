from wad2_entry import wad2_entry
from wad2_header import wad2_header

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

      @staticmethod
      def read(data):
         '''
         This fuction returns data
         from wad2 file.
         But, you need read full wad2 file
         and give result of this

         example:
         file = open(filename, "rb")
         data = file.read()
         file.close()

         file = wad2.read(data)
         '''

         file = wad2()
         file.header = wad2_header.read(data)
         
         file.entries = dict()

         for index in range(file.header.numentries):
            entry = wad2_entry.read(data, file.header.diroffset, 32 * index)
            file.entries[entry.name] = entry


         return file