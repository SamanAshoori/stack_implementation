#Welcome to the Stack Implementation in Python

class Stack:
#======== class start ==========
    def __init__(self, height):
        self.height = height
        self.top = -1
        self.data = []
    
    def push(self,x):
        if(self.top == (self.height - 1)):
            print('Cannot Push - stack is full')
        else:
            self.top = self.top + 1
            self.data.insert(self.top, x)
    
    def pop(self):
        if(self.top == -1):
            print('nothing to pop')
        else:
            del self.data[self.top]
            self.top -= -1


#============ class end ===================
print('Test')

s1 = Stack(5)
print(s1.height)
print(s1.top)
print(s1.data)
#test to see if it works
s1.push(12)
s1.push("42")
print("top of stack is"  + str(s1.top))
print("data in stack is" + str(s1.data))