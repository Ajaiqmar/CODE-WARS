class Node:
    def __init__(self,x):
        self.val = x
        self.next = None

def valid_parentheses(string):
    Stack = None
    
    for i in string:
        
        if(i == '('):
            temp = Node(i)
            
            if(Stack == None):
                Stack = temp
            else:
                temp.next = Stack
                Stack = temp
                
        elif(i == ')'):
            if(Stack == None):
                return False
            else:
                Stack = Stack.next
    
    if(Stack != None):
        return False
    
    return True
