def product_except_self(arr):
  answer = [1]*len(arr)
  i=0, j=len(arr)
  
  for i in arr:
    answer[i]=product_except_self(answer[i+1])
    answer[j]=product_except_self(answer[j-1])
  answer = answer[i]*answer[j]
  return answer
  
    
    
    
