from tkinter import N


matrix = [[1,3]]
target = 2

def searchMatrix(matrix,target):
    ROWS,COLS = len(matrix), len(matrix[0])

    top,bot = 0, ROWS - 1

    while top <= bot:

        row = (top + bot) // 2

        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break

    if not (top <= bot):
        return False
    
    row = (top + bot) // 2

    l,r = 0, COLS

    while l <= r:

        mid_val = (l + r) // 2

        if target < matrix[row][mid_val]:
            r = mid_val - 1
        elif target > matrix[row][mid_val]:
            l = mid_val + 1
        else:
            return True
    return False

print(searchMatrix(matrix,target))