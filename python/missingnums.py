#get two inputs. one is n and other is list of nums
#sort the list out
#make a placeholder var starting with 1
#compar with and increase iter by 1 uptill the nums[i] is not equal to placeholder
#print the number where not equal

n = int(input())
nums = list(map(int, input().split()))

sortednums = sorted(nums)
#print(sortednums)

place = 1

if (2 <= n and n <= 200000):
    for i in range(len(sortednums)):
        #print(i+1, "sortednums: ", sortednums[i])
        if ((i+1) == sortednums[i]):
            place += 1
        else:
            print(place)
            break
    if place == n:
        print(place)
#    for i in sortednums:
#        if (place == i):
#            place += 1
#        else:
#            print(place)
#            break

