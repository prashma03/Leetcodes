#Given an array nums containing n distinct numbers in the range [0,n], return only the number in the range that is missing from the array.
#input :[3,0,1]
#output: 2
def missing_numbers(nums):
  for i in range (len(nums)+1):
    if i not in nums:
      return i
input = [3,0,1]
print(missing_numbers(input))
