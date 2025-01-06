s = sum(map(int, input().split()))
p1 = 1
p2 = 9
while True:
    if p1 + p2 < s:
        p1 += 1
    elif p1 + p2 > s:
        p2 -= 1
    else:
        break
print(p1 + p2)