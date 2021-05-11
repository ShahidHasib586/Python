n = str(input())
l = len(n)
if l > 10:
    print(n[0], end='')
    print(l-2, end='')
    print(n[l-1])
else:
    print(n)