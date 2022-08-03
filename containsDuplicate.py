nums = [1,2,3,1]

lookup = {}

for i in range(len(nums)):
    if nums[i] in lookup:
        print(True)
    lookup[i] = nums[i]

