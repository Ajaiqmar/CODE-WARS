def hcf(a,b):
    if(b==0):
        return a
    else:
        return hcf(b,a%b)

def convert_fracts(lst):
    if(len(lst) == 0):
        return lst
    
    lcm = lst[0][1]
    
    for i in range(1,len(lst)):
        lcm = (lcm*lst[i][1])//hcf(max(lcm,lst[i][1]),min(lcm,lst[i][1]))
    
    for i in range(len(lst)):
        lst[i][0] = lst[i][0]*(lcm//lst[i][1])
        lst[i][1] = lcm
    
    return lst
