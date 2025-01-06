a, b = map(int, input().split())
p = max(a, b)
q = min(a, b)
while True:
    p %= q
    t = p
    p = q
    q = t
    if q == 0:
        break
a /= p
b /= p
print(int(p * (a + b)))