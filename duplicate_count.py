def duplicate_count(text):
    text = text.lower()
    d = {}
    ans = 0
    
    for i in text:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
            
        if(d[i]==2):
            ans = ans+1
    
    return ans
