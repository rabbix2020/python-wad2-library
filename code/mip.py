import struct

@staticmethod
def read(data: list) -> list:
   # for some unknown reasons texture starts with name with length of 16 bytes
   texture_data = data[16:]

   size = (struct.unpack("i", texture_data[:4])[0], struct.unpack("i", texture_data[4:8])[0])
   texture_data = texture_data[24:]

   texture_pack = [None] * 4
   texture_pack[0] = (size, texture_data[0:(size[0] * size[1])])
   for quality in range(4):
      texture_pack[quality] = (size, texture_data[0:(size[0] * size[1])])
      texture_data = texture_data[size[0] * size[1]:]
      size = (size[0] // 2, size[1] // 2)

   return list(texture_pack)
