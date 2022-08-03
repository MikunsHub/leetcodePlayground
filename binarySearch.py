
from xml.dom.minidom import Element


def linear_search(num_list,target):
    for index, element in enumerate(num_list):
        if element == target:
            return index
    return -1

def binary_search(num_list,target):
    left_index = 0
    right_index = len(num_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = num_list[mid_index]

        if mid_number == target:
            return mid_index
        
        if mid_number < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    
    return -1

def binary_search_recursive(num_list,target,left_index,right_index):   
    
    if right_index < left_index:
        return -1
    
    mid_index = (left_index + right_index) // 2

    if mid_index >= len(num_list) or mid_index < 0:
        return -1
    
    mid_number = num_list[mid_index]

    if mid_number == target:
        return mid_index
    
    if target > mid_number:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1
    
    return binary_search_recursive(num_list,target,left_index,right_index)
     


nums = [1,2,3,4,4,4,5,5,7,9,11]
target = 5

linear = linear_search(nums,target)
binary = binary_search(nums,target)
binary_recursive = binary_search_recursive(nums,target,0,len(nums))

print(f"Number found at index {linear} using linear search")
print(f"Number found at index {binary} using binary search")
print(f"Number found at index {binary_recursive} using binary_recursive search")


matrix = [[2,3,4,5],[10,11,16,20],[23,30,34,60]]

Rows, Cols = len(matrix),len(matrix[0])
print(Rows,Cols)
print(Rows-1)