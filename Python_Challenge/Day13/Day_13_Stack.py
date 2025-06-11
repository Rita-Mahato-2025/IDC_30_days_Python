class Stack:
    def __init__(self):
        self.stack = []

    # Push Method
    def push(self, item):
        self.stack.append(item)
        print(f"Pushed item: {item}")

    # Pop Method
    def pop(self):
        if not self.stack:
            print("Empty Stack. Cannot pop.")
        else:
            item = self.stack.pop()
            print(f"Popped: {item}")

    # Peek Method
    def peek(self):
        if not self.stack:
            print("Empty stack. Nothing to peek.")
        else:
            item = self.stack[-1]
            print(f"Top item: {item}")

# Create and use the stack
s = Stack()
s.push(10)
s.push(30)
s.push(50)
s.pop()
s.peek()
