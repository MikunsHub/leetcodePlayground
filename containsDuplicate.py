nums = [1,2,3,1]

lookup = {}

for i in range(len(nums)):
    if nums[i] in lookup:
        print(True)
    lookup[i] = nums[i]


# def containsDuplicate(nums):
#     lookup = set()

#     for num in nums:
#         if nums[num] in lookup:
#             return True
#         lookup[num] = nums[num]
#     return False

# print(containsDuplicate(nums))

