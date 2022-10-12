s = input()
n = len(s)
ans =""
for i in range(0,n,1):
    if s[i] != " ":
        ans += s[i]
print(ans)