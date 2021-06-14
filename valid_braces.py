class Node:
    def __init__(self,x):
        self.val = x
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        
    def push(self,x):
        temp = Node(x)
        if(self.head == None):
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp  
        
    def peek(self):
        return self.head.val
      
    def pop(self):
        self.head = self.head.next
            
        
def validBraces(string):
  
    stack = Stack()
    
    for i in string:
        if(i=='{' or i=='(' or i=='['):
            stack.push(i)
        else:
            if(i=='}' and stack.head!=None and stack.peek()=='{'):
                stack.pop()
            elif(i==']' and stack.head!=None and stack.peek()=='['):
                stack.pop()
            elif(i==')' and stack.head!=None and stack.peek()=='('):
                stack.pop()
            else:
                return False
        
    if(stack.head != None):
        return False
    else:
        return True
