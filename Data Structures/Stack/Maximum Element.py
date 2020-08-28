class Stack():
	
  def __init__(self):
    self.stack = []
    self.SupportStack = []
    
  def push(self, data):
    self.stack.append(data)
    if self.SupportStack == []:
      self.SupportStack.append(data)
    elif self.top() >= self.SupportStack[-1]:
      self.SupportStack.append(self.top())
    
  def pop(self):
    if self.top() == self.SupportStack[-1]:
      self.SupportStack.pop()
    return self.stack.pop()
    
  def top(self):
    return self.stack[-1]
    
  def is_empty(self):
    return self.stack == []
  
  def getMax(self):
    return self.SupportStack[-1]

if __name__ == "__main__":        
    mystack = Stack()
    Q = int(input())
    for i in range(Q):
        a = list(map(int,input().split()))
        if a[0] == 1:     
            mystack.push(a[1])
        elif a[0] == 2:
            mystack.pop()
        elif a[0] == 3:
            print(mystack.getMax())