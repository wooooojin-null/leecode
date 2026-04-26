nums = [2,7,11,15]
target = 9
memory = []
ans = []

for i in nums:
    if i in memory:
        if nums.count(i) >= 2:
            ans.append(nums.index(i))
            ans.append(nums.index(i, nums.index(i) + 1))
        else:
            ans.append(nums.index(target - i))
            ans.append(nums.index(i))
        break
    else:
        memory.append(target - i)

print(ans)