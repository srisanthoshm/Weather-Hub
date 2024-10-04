nums=[2,7,11,15]
target=9
d={}
n=len(nums)
for i in range(n):
    d[nums[i]]=i
print(d)
for i in range(n):
    diff=target-nums[i]
    if diff in d and d[diff]!=i:
        print([i,d[diff]])

