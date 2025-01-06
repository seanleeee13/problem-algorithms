a, b = input().split()
a = list(a)
b = list(b)
a.reverse()
b.reverse()
if len(a) > len(b):
    b = ["0"] * (len(a) - len(b)) + b
elif len(a) < len(b):
    a = ["0"] * (len(b) - len(a)) + a
up = 0
ans = []
numlist = [["0", "1"], ["0", "2"], ["0", "3"], ["0", "4"], ["0", "5"], ["0", "6"], ["0", "7"], ["0", "8"], ["0", "9"], ["1", "0"], ["1", "1"], ["1", "2"], ["1", "3"], ["1", "4"], ["1", "5"], ["1", "6"], ["1", "7"], ["1", "8"], ["1", "9"]]
intlist = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
def plus(up, n, m):
    numiter = iter(numlist)
    intiter1 = iter(intlist)
    intiter2 = iter(intlist)
    l = ["0", "0"]
    if up == "1":
        l = next(numiter)
    if n != "0":
        while True:
            l = next(numiter)
            if next(intiter1) == n:
                break
    if m != "0":
        while True:
            l = next(numiter)
            if next(intiter2) == m:
                break
    return l
for x, y, i in zip(a, b, range(len(a))):
    up, temp = plus(up, x, y)
    ans.append(temp)
if up == "1":
    ans.append("1")
ans.reverse()
print(*ans, sep="")