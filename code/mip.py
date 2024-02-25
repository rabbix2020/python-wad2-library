import struct

@staticmethod
def read(data: list) -> dict:
   texture = [None, None, None, None]
   # for some unknown reasons texture starts with name with length of 16 bytes
   texture_data = data[16:]
   # for some unknown reasons wad2 format stores size of mip texture this way
   size = (texture_data[0], texture_data[4])
   texture_data = texture_data[24:]   

   texture[0] = texture_data[0:size[0]*size[1]]
   texture[1] = texture_data[size[0]*size[1]:size[0]*size[1]+(size[0]//2*size[1]//2)]
   texture[2] = texture_data[size[0]*size[1]+(size[0]//2*size[1]//2):size[0]*size[1]+(size[0]//2*size[1]//2)+(size[0]//4*size[1]//4)]
   texture[3] = texture_data[size[0]*size[1]+(size[0]//2*size[1]//2)+(size[0]//4*size[1]//4):size[0]*size[1]+(size[0]//2*size[1]//2)+(size[0]//4*size[1]//4)+(size[0]//8*size[1]//8)]

   return {"size": size, "texture": texture}