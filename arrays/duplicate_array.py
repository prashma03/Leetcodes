#Given an integer array num, return true if value appears at least twice in the array, and retuen false if every element is distinct.
def duplicate_array(nums):
  for i in range (0,len(nums)):
    for j in range (i+1, len(nums)):
      if nums[i] == nums[j]:
        return True
  return False
nums = [1,2,1,1,3]
print(duplicate_array(nums))

#Another approach
def duplicate_array(nums):
  set_nums = set(nums)
  if len(nums)==len(set_nums):
    return False
  else:
    return True
nums = [1, 2, 1, 1, 3]
print(duplicate_array(nums))
  
