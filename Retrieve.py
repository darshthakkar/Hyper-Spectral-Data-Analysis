# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 22:58:54 2017

@author: Darsh
"""

from spectral import *
import pylab as pb 
import numpy as np
import pandas as pd
import matplotlib.cm as cm
import matplotlib.pyplot as plt

ls1=pd.read_csv("Main_206/difference_sum1.csv")
diff1=ls1["Difference"]
ls2=pd.read_csv("Main_147/difference_sum2.csv")
diff2=ls2["Difference"]
mat=[]
i=0


while i<205:
    row1=[]
    j=0
    while j<205:
        row1.append(diff1[i*205+j])
        j+=1
    mat.append(row1)
    i+=1
    
agg=[]  
difference_array1=[]
for i in range (0,204):
    for j in range (0,204):
        if mat[i][j]<70:
            difference_array1.append(1)            
        else:
            difference_array1.append(0)
final1=np.asanyarray(difference_array1)
final_reshaped1 = final1.reshape(204,204)
#print ("For subest_206 \n\n\n\n")
#pb.imshow(final_reshaped1)


k=0
while k<146:
    row2=[]
    j=0
    while j<146:
        row2.append(diff2[k*146+j])
        j+=1
    mat.append(row2)
    k+=1

difference_array2=[]
for i in range (0,145):
    for j in range (0,145):
        if mat[i][j]<50:
            difference_array2.append(1)
        else:
            difference_array2.append(0)

final2=np.asanyarray(difference_array2)
final_reshaped2 = final2.reshape(145,145)
#print ("For subest_147")
#pb.imshow(final_reshaped2)

f=pb.figure()

f.add_subplot(1,2,1)
pb.imshow(final_reshaped1)

f.add_subplot(1,2,2)
pb.imshow(final_reshaped2)



pb.show()