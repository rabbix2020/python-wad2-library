import struct

@staticmethod
def read(data: list) -> list:
   width = struct.unpack("i", data[:4])[0]
   height = struct.unpack("i", data[4:8])[0]
   texture = []

   for i in range(height):
      texture.append(data[8+(width*i):8+(width*(i+1))])

   return list(texture)