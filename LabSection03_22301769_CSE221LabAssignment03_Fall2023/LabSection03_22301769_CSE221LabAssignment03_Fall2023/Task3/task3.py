# -*- coding: utf-8 -*-
"""Task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HtrU_3J96o386ggkZzcr55BZWPr4vVhx
"""

inf = open("input3.txt", 'r')
outf = open("output3.txt", 'w')

n = int(inf.readline().strip())
data = list(map(int, (inf.readline().strip().split())))

def dvd_nd_cnqr(data, cnt=0):
    if len(data) <= 1:
        return data, cnt

    mid = len(data)//2
    l = data[:mid]
    r = data[mid:]


    srt_l, cnt_l = dvd_nd_cnqr(l, cnt)
    srt_r, cnt_r = dvd_nd_cnqr(r, cnt)

    srt_all = []

    i, j = 0, 0

    while i < len(srt_l) and j < len(srt_r):
        if srt_l[i] < srt_r[j]:
            srt_all.append(srt_l[i])
            i += 1

        elif srt_l[i] > srt_r[j]:
            srt_all.append(srt_r[j])

            cnt += len(srt_l) - i
            j += 1

        elif srt_l[i] == srt_r[j]:
            srt_all.append(srt_l[i])
            srt_all.append(srt_r[j])
            i += 1
            j += 1

    srt_all.extend(srt_l[i:])
    srt_all.extend(srt_r[j:])

    return srt_all, cnt_l+cnt+cnt_r

outf.write(str(dvd_nd_cnqr(data)[1]))

inf.close()
outf.close()