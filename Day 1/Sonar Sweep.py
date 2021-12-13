"""
count = 0
with open("inputs.txt") as inputs:
    num = inputs.read()
    nums = [int(x) for x in num.split()]
for idx in range(len(nums) - 1):
    if nums[idx - 1] < nums[idx]:
        count += 1
print(count)
"""
count = 0
with open("inputs.txt") as inputs:
    num = inputs.read()
    nums = [int(x) for x in num.split()]


sums = []
for idx in range(len(nums)):
    sums.append(sum(nums[idx : idx + 3]))


for idx in range(len(sums) - 1):
    if sums[idx] > sums[idx - 1]:
        count += 1

print(count)
