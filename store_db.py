# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 19:02:58 2017 
@author: Darsh
"""


from spectral import *
import pylab as pb
import numpy as np
import pandas as pd
import math

def subpix(ref,pix,size):
    i=0
    sum1=0
    while i<size:
        sum1+=(ref[i]-pix[i])
        i+=1
    return sum1  

img = open_image('D:/Darsh/Nirma/Semester 6/Mini Project/Final/206_region/new.hdr').load()
#view = imshow(img)
'''
reference=[]
for i in range(0,425):
        reference.append(img[30,70,i])
x = np.linspace(0,424,425)
print("\n Bands for the reference pixel for subset_206: \n \n ")
print(reference)
pb.plot(x,reference)
pb.show()
'''

diff=0
diffset=[]
csvlist=[]

ls1=pd.read_csv("reference/ref_value.csv")
ref2=ls1["Value"]

#ref2=[]
#for z in range(70,91):
  #  ref2.append(reference[z])
for i in range(0,154):
    rowset=[]    
    for j in range(0,154):
        csvrow=[]
        sample=[]
        for k in range(70,91):
            sample.append(img[i,j,k])        
        sum1 = subpix(ref2,sample,21)
        sum1=np.absolute(sum1)
        csvrow.append(i)
        csvrow.append(j)
        csvrow.append(sum1)
        if sum1 < 70:
            csvrow.append("YES")
        else:
            csvrow.append("NO")

        csvlist.append(csvrow)          
        rowset.append(sum1)
    print(i)
    diffset.append(rowset)
csvfile=pd.DataFrame(csvlist,columns=["X Co-ordinate","Y Co-ordinate","Difference","Agriculture Land Class"])  
csvfile.to_csv("147_region/147_region4.csv")  
print(diffset)



'''
sample=[]
for k in range(0,425):
     sample.append(img[70,30,k])        
sum1 = subpix(reference,sample,425)  
print(sum1)     '''
#region_interested1 = img [70,30,0]
#arr=region_interested1.load()
#print (region_interested1)
#pylab.plot(x,arr)
#print(region_interested1.reshape(425,-1))
#a = region_interested1[0,:,:]
#a = np.reshape(region_interested1,(25,1,4250))
#kmeans = KMeans(n_clusters = 3,random_state = 0 ).fit(gray)
"""
(a,s)=kmeans(a)
myavg_int1=sum(s)/10
total=0
#for i in range(10)      
pb.figure()
 ------------------------------b.hold(1)
print (s)
print ("Graph of s")
#pb.plot(s)
pb.plot(myavg_int1)
pb.show()
"""