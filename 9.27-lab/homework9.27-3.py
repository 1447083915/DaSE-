list = input()
n = len(list)
max = 0
count = 1
for i in range(1,n,1):
    if list[i] == list[i-1]:
        count += 1
    else:
        count = 1
    if count > max:
        max = count
print(max)