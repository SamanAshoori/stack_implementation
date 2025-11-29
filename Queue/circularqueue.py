class Queue:
    def init(self,size):
        self.size = size
        self.front = -1
        self.tail = -1
        self.isEmpty = True
        #To simulate C++ memory management
        self.data = ['None'] * size
    
    def enqueue(self,value:int) -> bool:
        #input a int but return a boolean value
        if(self.isEmpty == True):
            self.front = 0
            self.tail = 0
            self.data