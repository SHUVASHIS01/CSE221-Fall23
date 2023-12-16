# -*- coding: utf-8 -*-
"""Task4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HtrU_3J96o386ggkZzcr55BZWPr4vVhx
"""

import math

inf= open("input4.txt", 'r')

outf = open("output4.txt", 'w')

n = int(inf.readline().strip())
data = list(map(int, (inf.readline().strip().split())))


def dvd_nd_cnqr(data, max_v = -math.inf):

    if len(data) == 1:
        return data, -math.inf

    if len(data) == 2:
        temp = data[0] + pow(data[1], 2)
        if temp >= max_v:
            max_v = temp
        return data, max_v

    mid_ind = len(data)//2
    l = data[:mid_ind]
    r = data[mid_ind:]

    l_part, l_max = dvd_nd_cnqr(l, max_v)
    r_part, r_max = dvd_nd_cnqr(r, max_v)
    merged_array = []

    if l_max >= r_max:
        max_v = l_max
    else:
        max_v = r_max

    b_max = max(l_part)
    i = 0
    while i < len(r_part):
        if max_v <= b_max + pow(r_part[i] , 2):
            max_v = b_max + pow(r_part[i] , 2)
        i += 1

    merged_array.extend(l_part)
    merged_array.extend(r_part)

    return merged_array, max_v

outf.write(str(dvd_nd_cnqr(data)[1]))

inf.close()
outf.close()