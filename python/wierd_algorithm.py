#inpiut n
#if n is even, divide by two
#if odd multiply by 3 and add 1
# if 1 then stop
#print all nuimbers

n = int(input())
if (n >= 1 and n <= 1000000):
    while (n != 1):
        print(n, end=" ")
        if (n%2 == 0):
            n = n//2
        else:
            n = (n*3) + 1
    print(n)
