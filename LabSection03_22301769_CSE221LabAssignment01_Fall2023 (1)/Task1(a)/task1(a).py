# -*- coding: utf-8 -*-
"""Task1(a).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CoIc0KgVH8R1GQ-1HndrHI4cOWhtvBRF
"""

file=open("/content/Task1(a)/input1a.txt", "r")
text=file.read()
print(text)

file=open("output1a.txt", "a")
file.write("new folder")
file.close()

file=open("/content/Task1(a)/input1a.txt", "r")
text=file.readline()
f=open("/content/Task1(a)/output1a.txt", 'w')
for i in range (int(text)):
  text1=file.readline()
  if int(text1)%2==0:
    f.writelines(f'{int(text1)} is an Even number\n')
  else:
    f.writelines(f'{int(text1)} is an Odd number\n')
f.close()