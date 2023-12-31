# -*- coding: utf-8 -*-
"""Task5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iGilsVwbJs9qDAcPyo9K2iW6pinBTR_m
"""

inf = open("input5.txt", 'r')
outf = open("output5.txt", 'w')
v, e, d = list(map(int, inf.readline().strip().split()))
vistd = [0 for i in range(v+1)]
lvl = [0 for y in range(v+1)]
prnt = [0 for z in range(v+1)]
ad_l = [[]for i in range(v+1)]
for i in range(e):
    f, t = list(map(int, inf.readline().strip().split()))
    ad_l[f].append(t)
    ad_l[t].append(f)

def BFS_trvrsl(ad_l, src):
    queue = []
    queue.append(src)
    vistd[src] = 1
    lvl[src] = 0
    prnt[src] = src

    while queue:
        temp = queue.pop(0)
        for x in ad_l[temp]:
            if vistd[x] == 0:
                vistd[x] = 1
                lvl[x] = lvl[temp] + 1
                prnt[x] = temp
                queue.append(x)
            if x == d:
                break
src = 1
BFS_trvrsl(ad_l, src)
print(f"Time : {lvl[d]}", file=outf)
asnr = []
while True:
    asnr.append(d)
    if d == src:
        break
    d = prnt[d]
asnr.reverse()
print("Shortest Path: ", end="", file=outf)

for x in asnr:
    print(x, end = " ", file=outf)
inf.close()
outf.close()