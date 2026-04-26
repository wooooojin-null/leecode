x = str(121)
list_x = []

for i in x:
    list_x.append(i)

if list_x == list_x[::-1]:
    ans = True
else:
    ans = False

print(ans)