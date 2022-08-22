
def twoSum2(nums,target):
    l,r = 0, len(nums)-1

    while l < r:
        currSum = nums[l] + nums[r]

        if currSum > target:
            r -= 1
        elif currSum < target:
            l += 1
        else: 
            return [ l+1, r+1 ]
    return

print(twoSum2(nums=[1,3,4,5,7,10,11],target=9))