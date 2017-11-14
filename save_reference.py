# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:34:30 2017

@author: Darsh
"""

from spectral import *
import pylab as pb
import numpy as np
import pandas as pd
import math
img = open_image('D:/Darsh/Nirma/Semester 6/Mini Project/subset_206.hdr').load()
#view = imshow(img)
reference=[]
for i in range(0,425):
        reference.append(img[30,70,i])
x = np.linspace(0,424,425)
print("\n Bands for the reference pixel for subset_206: \n \n ")
print(reference)
pb.plot(x,reference)
pb.show()

ref2=[]
csvlist=[]
for z in range(70,91):
    csvrow=[]
    ref2.append(reference[z])
    csvrow.append(z)
    csvrow.append(reference[z])
    csvlist.append(csvrow)
    
csvfile=pd.DataFrame(csvlist,columns=["Band_Number","Value"])  
csvfile.to_csv("reference/ref_value.csv")  