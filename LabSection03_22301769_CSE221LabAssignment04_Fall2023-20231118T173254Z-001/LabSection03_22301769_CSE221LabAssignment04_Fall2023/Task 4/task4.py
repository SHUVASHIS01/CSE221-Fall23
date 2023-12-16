# -*- coding: utf-8 -*-
"""Task4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iGilsVwbJs9qDAcPyo9K2iW6pinBTR_m
"""

inf = open("input4.txt", 'r')
outf = open("output4.txt", 'w')
v, e = list(map(int, inf.readline().strip().split()))
visit = [0 for i in range(v+1)]
ad_l = [[]for i in range(v+1)]
for i in range(e):
    f, t = list(map(int, inf.readline().strip().split()))
    ad_l[f].append(t)

def cycle_detection(ad_l, select):
    visit[select] = 1
    for ad_nd in ad_l[select]:
        if visit[ad_nd] == 0:
            Got_cycle = cycle_detection(ad_l, ad_nd)
            if(Got_cycle):
                return True
        elif visit[ad_nd] == 1:
            return True
    visit[select] = 2
    return False

Cycle_exist = False
for i in range(1, v+1):
    if visit[i] == 0:
        is_Cyclic= cycle_detection(ad_l, i)
        if is_Cyclic:
            Cycle_exist = True
            break

if Cycle_exist:
    print("YES", file=outf)
else:
    print("NO", file=outf)
inf.close()
outf.close()