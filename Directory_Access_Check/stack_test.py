#Checking basic access of Stack class from different directory
from Stack.stack import Stack
s = Stack(10) # Stack requires a height argument
s.push(1)
s.push(2)

print(s.pop())  # Should print 2
