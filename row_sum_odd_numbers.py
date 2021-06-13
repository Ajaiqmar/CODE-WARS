# APPROACH - 1
def row_sum_odd_numbers(n):
    #your code here
    v = ((n-1)*n)+1
    ans = 0
    
    for i in range(n):
        ans += v
        v += 2
    
    return ans
  
  # APPROACH - 2
  def row_sum_odd_numbers(n):
    #your code here
    return n**3
  
