
def maxArea(height) -> int:
    
    res = 0

    left = 0
    right = len(height) - 1

    while left < right:
        area = (right - left) * min(height[left],height[right])
        res = max(res,area)

        if height[left]  < height[right]:
            left += 1
        else:
            right -= 1
        
    return res

height = [1,2]
print(maxArea(height))