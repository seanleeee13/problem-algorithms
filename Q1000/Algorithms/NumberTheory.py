from functools import reduce
a, b = map(int, input().split())
div = 2
al = []
while a > 1:
    if a % div == 0:
        al.append(div)
        a //= div
    else:
        div += 1
        if div > int(a ** 0.5):
            div = a
div = 2
bl = []
while b > 1:
    if b % div == 0:
        bl.append(div)
        b //= div
    else:
        div += 1
        if div > int(b ** 0.5):
            div = b
isn = []
if len(al) > len(bl):
    for i in bl:
        if i in al:
            al.remove(i)
            bl.remove(i)
            isn.append(i)
else:
    for i in al:
        if i in bl:
            al.remove(i)
            bl.remove(i)
            isn.append(i)
if len(al) == 1:
    am = al[0]
elif len(al) == 0:
    am = 1
else:
    am = reduce(lambda x, y: x * y, al)
if len(bl) == 1:
    bm = bl[0]
elif len(bl) == 0:
    bm = 1
else:
    bm = reduce(lambda x, y: x * y, bl)
if len(isn) == 1:
    im = isn[0]
elif len(isn) == 0:
    im = 1
else:
    im = reduce(lambda x, y: x * y, isn)
print(im * (am + bm))