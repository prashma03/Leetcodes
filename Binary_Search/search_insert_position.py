# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be inserted to keep the array sorted.
items = [1,3,5,6]
target = 5
def find_target(items, target):
  left, right = 0,len(items)-1
 
  while left  <=  right:
     mid = (left+right)//2
    if items[mid] == target:
      return mid
    elif target>items[mid]:
       left = mid+1
    else:
      right = mid-1
  return left
a = find_target(items,target)
print(a)
     
