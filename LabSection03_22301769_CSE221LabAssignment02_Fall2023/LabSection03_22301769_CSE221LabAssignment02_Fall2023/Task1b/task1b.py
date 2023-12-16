# -*- coding: utf-8 -*-
"""Task1b.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E7JHAQ_67ZGx30wd-cawmAyfyVSyHsIU
"""

f1=open('input1b.txt', 'r')
f2=open('output1b.txt', 'w')
n, t = list(map(int, (f1.readline().strip().split())))
k=list(map(int, (f1.readline().strip().split())))
d={}
possible=False
for i in range (n):
  r=(t-k[i])
  if r in d:
    f2.write(f'{d[r]} {i+1}')
    possible=True

  else:
    d[k[i]]=i+1

if not possible:
  f2.write(f'IMPOSSIBLE')
f2.close()