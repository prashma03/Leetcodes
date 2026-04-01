#Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
#Integers in each row are sorted in ascending from left to right.
#Integers in each column are sorted in ascending from top to bottom.
def searchMatrix(matrix, target):
    """
    Searches for a target value in a 2D matrix.
    
    Args:
    - matrix (List[List[int]]): m x n matrix sorted row-wise and column-wise
    - target (int): the value to search for
    
    Returns:
    - bool: True if target is found, False otherwise
    """
    
  if not matrix or not matrix[0]:
        # Empty matrix or empty rows
        return False

    # Start from the top-right corner
    row = 0
    col = len(matrix[0]) - 1

    # Loop until we go out of bounds
    while row < len(matrix) and col >= 0:
        current = matrix[row][col]
        
        if current == target:
            # Found the target
            return True
        elif current > target:
            # Current value too big, move left
            col -= 1
        else:
            # Current value too small, move down
            row += 1

    # Target not found
    return False

# Example usage:
matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17]
]
target = 5

print(searchMatrix(matrix, target))  #Output: True
