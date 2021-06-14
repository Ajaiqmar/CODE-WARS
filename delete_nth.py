def delete_nth(order,max_e):
    # code here
    ans = []
    d = {}
    
    for i in order:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
        
        if(d[i]<=max_e):
            ans.append(i)
        
    return ans
