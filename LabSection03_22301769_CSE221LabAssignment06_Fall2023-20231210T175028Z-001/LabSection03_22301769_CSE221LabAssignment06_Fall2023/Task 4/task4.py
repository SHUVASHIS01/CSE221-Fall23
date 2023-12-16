# -*- coding: utf-8 -*-
"""Task4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-qCDcd7HPu9WDt7sxRYf-QM0vx3oIiZS
"""

inf = open("input4.txt", 'r')
outf = open("output4.txt", 'w')
city, road = map(int, inf.readline().split())
ad_l = [ [] for i in range(city + 1) ]
vstd = [ 0 for i in range(city + 1) ]
for i in range(road):
    f, t, w = map(int, inf.readline().split())
    ad_l[f].append((t, w))
    ad_l[t].append((f, w))

def min_cst(ad_l, vstd):
    pq = []
    cst = 0
    vstd[1] = 1
    for i in ad_l[1]:
        pq.append(i)
    while pq:
        pq.sort(key = lambda x: x[1])
        u, w = pq.pop(0)
        if vstd[u] == 0:
            vstd[u] = 1
            cst += w
            for i in ad_l[u]:
                pq.append(i)
    return cst

print(min_cst(ad_l, vstd) , file = outf)
inf.close()
outf.close()