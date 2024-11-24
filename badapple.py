#!/bin/python
import cv2
from os import listdir
from os.path import isfile, join, abspath

bmpsPath = join(abspath("."), "bmps")

onlyfiles = [join(bmpsPath,f) for f in listdir(bmpsPath) if isfile(join(bmpsPath,f))]
onlyfiles.sort()
with open('src/image.h', 'w') as f:
    f.write(f"unsigned long frames[{len(onlyfiles)}][3] = \n")
    f.write("{")
    for bmp in onlyfiles:
        if bmp.endswith(".bmp"):
            binaryString = ""
            pixels = cv2.imread(bmp, 0)
            for row in range(len(pixels)):
                for col in range(len(pixels[0])):
                    if pixels[row][col] > 127:
                        binaryString += "1"
                    else:
                        binaryString += "0"
            f.write("{\n")
            f.write(f"{hex(int(binaryString[0:32], 2))},\n")
            f.write(f"{hex(int(binaryString[32:64], 2))},\n")
            f.write(f"{hex(int(binaryString[64:], 2))},\n")
            f.write("},\n")
    f.write("};\n")

