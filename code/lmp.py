import struct

@staticmethod
def read(data):
    length = int(len(data) / 3)
    lmp = []

    for index in range(length):
       color = [0, 0, 0]
       color[0] = int.from_bytes(struct.unpack("c", data[3*index:3*index+1])[0])
       color[1] = int.from_bytes(struct.unpack("c", data[3*index+1:3*index+2])[0])
       color[2] = int.from_bytes(struct.unpack("c", data[3*index+2:3*index+3])[0])
       lmp.append(color)

    return lmp