import sys
import os
from math import log
import numpy as np
import scipy as sp
import Image
import matplotlib.pyplot as plt
def saveimg(array,name):
    print name
    if array.shape[1]!=16:
        assert(False)
    b=int((array.shape[0]*16)**(0.5))
    b=2**(int(log(b)/log(2))+1)
    a=int(array.shape[0]*16/b)
    #print a,b,array.shape
    array=array[:a*b/16,:]
    array=np.reshape(array,(a,b))
    #print array.shape
    im = Image.fromarray(np.uint8(array))
    im.save('trainImage/'+name+'.jpg', "JPEG")
files=os.listdir('train')
c=0
for cc,x in enumerate(files):
    if '.bytes' != x[-6:]:
        continue
    print cc
    f=open('train/'+x)
    array=[]
    c+=1
    for line in f:
        xx=line.split()
        if len(xx)!=17:
            continue
        #if xx[1]=='??':
        #    break
        array.append([int(i,16) if i!='??' else 0 for i in xx[1:] ])
    saveimg(np.array(array),x)
    del array
    f.close()
print c

