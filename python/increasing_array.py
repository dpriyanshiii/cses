n = int(input())
xi = list(map(int, input().split()))

total = 0

#lets skip validation for now

for i in range(len(xi)-1):
    diff = 0
    if (xi[i] > xi[i+1]):
        diff = abs(xi[i+1] - xi[i])
        xi[i+1] = xi[i]

    total += diff
    
print(total)

#print(xi)
