def order(sentence):
    # code here
    ans = []
    sentence = sentence.split()
    
    for i in range(1,10):
        for j in sentence:
            if str(i) in j:
                ans.append(j)

    return " ".join(ans)
