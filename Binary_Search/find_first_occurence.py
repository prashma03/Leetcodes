# Given a sorted array (duplicates allowed) and a target, return the first index where the target appears.
# If it doesn’t exist, return -1.
nums = [1, 2, 2, 2, 3, 4]
target = 2

def find_first_occurence(nums,target):
  result = -1
  left,right = 0, len(nums)-1
  while left  <=  right:
    mid = (left+right)//2
    if nums[mid] == target:
      result = mid
      right = mid  -  1
    elif nums[mid]>target:
      right = mid -1
    else:
      left = mid+1
  return result
print(find_first_occurence(nums,target))
      
      
    
