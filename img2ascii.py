from PIL import Image
import numpy as np
import argparse
import os
from math import ceil, floor

#generated stuff
charset = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#%^&* .\'')
char_op = np.array(
      [ 0.23506246,  0.39377514,  0.39635825,  0.40330299,  0.36036418,
        0.3974169 ,  0.19775566,  0.58259581,  0.13622697,  0.20033877,
        0.35515562,  0.12030489,  0.41397417,  0.17793775,  0.28117722,
        0.40495448,  0.24818971,  0.27838238,  0.42816007,  0.54194368,
        0.29125556,  0.50899852,  0.24674995,  0.22125768,  0.2493754 ,
        0.30671184,  0.14444209,  0.18301927,  0.32771544,  0.47279272,
        0.3774296 ,  0.42290917,  0.17289858,  0.34389159,  0.49091679,
        0.33326276,  0.28888418,  0.15524031,  0.49210248,  0.20004235,
        0.29193309,  0.34240949,  0.21875926,  0.23929706,  0.5427906 ,
        0.45212788,  0.2650434 ,  0.51429176,  0.17988567,  0.36150752,
        0.34321406,  0.18915943,  0.23137836,  0.56519162,  0.4388736 ,
        0.44315054,  0.38471311,  0.54998941,  0.29193309,  0.40203261,
        0.40334533,  0.36019479,  0.19076858,  0.17137413,  0.63514715,
        0.        ,  0.66838874,  1.        ,  0.87533347,  0.87939869])
#functions
def Normalize(nparr):
    mi = nparr.min()
    ma = nparr.max()
    ret = (nparr-mi)/(ma-mi)
    return ret



def SelectClosest(inp):
    l = abs(char_op-inp)
    return np.where(l == min(l))[0][0]

def CalcAvgFromImg(img):
    arr = np.array(img)
    arr = np.average(arr, axis = 2)
    return np.average(arr)

#arguments
parser = argparse.ArgumentParser(description='Convert image to ASCII art.')
parser.add_argument('image', help='Image to be converted.')
args = parser.parse_args()
#args.image is the image filename

noextname,_ = os.path.splitext(args.image)


im = Image.open(args.image)
xmax, ymax = im.size

out_tmp = np.zeros( (ceil(xmax/8),ceil(ymax/13)) )


for y in range(0,ymax, 13):
    for x in range(0,xmax, 8):
        smim = im.crop((x,y,x+8,y+13))
        avg = CalcAvgFromImg(smim)
        out_tmp[floor(x/8)][floor(y/13)] = avg

out_tmp = Normalize(out_tmp)
print(out_tmp)
with open(noextname + '.txt','w') as f:
    for y in range(0,out_tmp.shape[1]):
        for x in range(0,out_tmp.shape[0]):
            cl = SelectClosest(out_tmp[x][y])
            char = charset[cl]
            f.write(char)
        f.write('\n')




