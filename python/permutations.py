#input int n
#output is series of nums back
n = int(input())

#if (1 <= n and n <= 1000000):   // dont be extra pri
if (n >= 4 or n == 1):
    l1 = []
    l2 = []
    for i in range(1, n+1):
        if (i%2 == 0):
            l2.append(i)
        else:
            l1.append(i)
    beautiful = l2 + l1
    print(*beautiful)
else:
    print("NO SOLUTION")
