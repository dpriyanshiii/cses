#anohter style
n = int(input())
nums = list(map(int, input().split()))

if (n >= 2 and n <= 200000):
    sumis = 0
    for i in range (len(nums)):
        sumis = sumis + nums[i]
    #print(sumis)

    apsumis = (n * (n + 1))/2

    missingnum = apsumis - sumis
    print(int(missingnum))
