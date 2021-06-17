def anagrams(word, words):
    ans = []
    d = {}
    
    for i in word:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    
    for i in words:
        flag = 0
        
        for j in set(i):
            if j not in d or d[j] != i.count(j):
                flag = 1
                break
        
        if(flag == 0):
            ans.append(i)
    
    return ans
