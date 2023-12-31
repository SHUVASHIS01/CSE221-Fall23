# -*- coding: utf-8 -*-
"""Task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iGilsVwbJs9qDAcPyo9K2iW6pinBTR_m
"""

inf = open("input2.txt", 'r')
outf = open("output2.txt", 'w')
v, e = list(map(int, inf.readline().strip().split()))
visit = [0 for i in range(v+1)]
ad_l = [[]for i in range(v+1)]
for i in range(e):
    f, t = list(map(int, inf.readline().strip().split()))
    ad_l[f].append(t)
    ad_l[t].append(f)

def BFS_trvrs(ad_l, src):
    queue = []
    queue.append(src)
    visit[src] = 1
    while queue:
        temp = queue.pop(0)
        print(temp, end=" ", file=outf)
        for x in ad_l[temp]:
            if visit[x] == 0:
                visit[x] = 1
                queue.append(x)
src = 1
BFS_trvrs(ad_l, src)
inf.close()
outf.close()