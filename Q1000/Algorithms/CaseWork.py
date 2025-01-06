s = "".join(input().split())
for i in range(1, len(s)):
    s1 = s[:i]
    s2 = s[i:]
    if s2[0] == "0":
        continue
    else:
        print(int(s1) + int(s2))