# -*- coding: utf-8 -*-
"""Task2b.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E7JHAQ_67ZGx30wd-cawmAyfyVSyHsIU
"""

str1="input2b.txt"
str2="output2b.txt"
inp=open(str1,"r")
otp=open(str2,"w")
leng1=int(inp.readline())
arr1=inp.readline().split()
leng2=int(inp.readline())
arr2=inp.readline().split()
k=leng1+leng2
arr=[None]*k
l=0
i=0
j=0
while l<k:
  if i!=leng1 and j !=leng2:
    if int(arr1[i])<int(arr2[j]):
        arr[l]=int(arr1[i])
        i+=1
    elif int(arr1[i])>int(arr2[j]):
        arr[l]=int(arr2[j])
        j+=1
    else:
        arr[l]=int(arr1[i])
        l+=1
        arr[l]=int(arr2[j])
        i+=1
        j+=1

  else:
    if i==leng1:
        arr[l]=int(arr2[j])
        j+=1
    else:
        arr[l]=int(arr1[i])
        i+=1
  l+=1

otp.write(str(arr))


inp.close()
otp.close()