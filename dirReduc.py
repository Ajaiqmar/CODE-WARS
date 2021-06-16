def dirReduc(arr):
    Stack = []
    
    for i in arr:
        if(len(Stack) == 0):
            Stack.append(i)
        else:
            ch = Stack[-1]
            if(((i[0]=='N' or i[0]=='n') and (ch[0]=='S' or ch[0]=='s')) or ((i[0]=='S' or i[0]=='s') and (ch[0]=='N' or ch[0]=='n'))):
                Stack.pop(-1)
            elif(((i[0]=='E' or i[0]=='e') and (ch[0]=='W' or ch[0]=='w')) or ((i[0]=='W' or i[0]=='w') and (ch[0]=='E' or ch[0]=='e'))):
                Stack.pop(-1)
            else:
                Stack.append(i)
    
    return Stack
