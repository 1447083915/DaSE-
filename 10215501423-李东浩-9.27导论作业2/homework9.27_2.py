list = [1,2,3,4,5]
n = len(list)
for i in range(n-1,-1,-1):
    print(list[i])

while n-1>=0:
    print(list[n-1])
    n -= 1

list_temp = list[::-1]
print(list_temp)