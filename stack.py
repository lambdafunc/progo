class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            return

        self.stack.pop()

    def printstack(self):
        print(self.stack)


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

stack.printstack()

stack.pop()
stack.printstack()
stack.pop()
stack.printstack()
stack.pop()
stack.printstack()
stack.pop()
stack.printstack()
stack.pop()
stack.printstack()
stack.pop()
stack.printstack()
stack.pop()
stack.printstack()
