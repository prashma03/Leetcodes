def last_occurence_index(nums,target):
  result = -1
  left, right=0, len(nums)-1
  while left <= right:
    mid = (left+right)//2
    if nums[mid] == target:
      result = mid
      left = mid+1
    elif nums[mid]<target:
      left = mid+1
    else:
      right = mid -1
  return result
nums = [1, 2, 2, 2, 3, 4]
target = 2
print(last_occurence_index(nums,target))
