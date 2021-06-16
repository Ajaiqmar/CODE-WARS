def duplicate_encode(word):
    word = word.lower()
    d = {}
    ans = ""
    
    for i in word:
        if i not in d:
            d[i]='('
        else:
            d[i]=')'
    
    for i in word:
        ans += d[i]
        
    return ans
