class Stack:

   def __init__(self, items=None, limit=100):
    if items is None:
        items = []
    self.stack = items
    self.limit = limit

        

    def isEmpty(self):
     return len(self.stack) == 0

    def push(self, item):
     self.stack.append(item)
     print("Pushed item: " + str(item))

        

    def pop(self):
     if self.isEmpty():
        return "Stack is empty"
     return self.stack.pop()


    def peek(self):
     if self.isEmpty():
        return "Stack is empty"
     return self.stack[-1]  # Return the top element of the stack

       
    
    def size(self):
     if self.isEmpty():
        return 0  # Stack is empty, so the size is 0
     return len(self.stack)

        

    def full(self):
     return len(self.stack) == self.max_size


      

    def search(self, target):
     if self.isEmpty():
        return "Stack is empty"
    
    # Iterate through the stack from the top to bottom
     for i in range(len(self.stack) - 1, -1, -1):
         if self.stack[i] == target:
                 return len(self.stack) - i  # Return position from the top (1-based index)

     return f"{target} not found in the stack"

       
