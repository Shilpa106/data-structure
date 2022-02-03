# # stack implementations using list

# stack=[]

# # append() function to push element in the stack
# stack.append('a')
# stack.append('b')
# stack.append('c')

# print('Initial stack')

# print(stack)

# # pop() function to pop element from stack in LIFO order
# print('\n Elements popped from stack:')
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print('\nStack after elements are popped:')

# print(stack)
# print(stack.pop())

# # time complexity=O(n)

# # implementations using collections.deque:
# from collections import deque

# stack=deque()

# # append() function to push element in the stack
# stack.append('a')
# stack.append('b')
# stack.append('c')

# print('Initial stack:')
# print(stack)

# # pop in lifo order
# print('\nElements popped from stack:')
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print('\n Stack after elements are popped:')
# print(stack)

# # print(stack.pop())

# # stack implementations using queue module
# from queue import LifoQueue

# # Initialization a stack
# stack = LifoQueue(maxsize=3)
# print(stack)
# # qsize() show the no of Elements in the stack
# print(stack.qsize())

# # put() to push element in the stack
# stack.put('a')
# stack.put('b')
# stack.put('c')

# print("Full:", stack.full())
# print("Size:", stack.qsize())

# # get() function to pop element from stack in LIFO order
# print('\nElements popped from the stack')
# print(stack.get())
# print(stack.get())
# print(stack.get())

# print("\nEmpty:", stack.empty())


# stack implementation using linked list node class

class Node:
    def __init__(self, value):
        self.value =value
        self.next=None

class Stack:
    # initializing a stack use a dummy node, which is easier for handling edge cases.
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    # string representation of the stack
    def __str__(self):
        cur = self.head.next
        # print("ffdfd",self.head)
        print("91",cur)
        # print("92",cur.value)
        out=""
        while cur:
            out+=str(cur.value) + "->"
            print("outtttttttttttttttttttttttttttt",out)
            cur = cur.next
        return out[:-3]

    # Get the current size of the stack
    def getSize(self):
        return self.size

    # Check if the stack is empty
    def isEmpty(self):
        return self.size==0

    # get the top item of the stack
    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value

    # Push a value into the stack
    def push(self, value):
        node=Node(value)
        node.next=self.head.next
        self.head.next=node
        self.size+=1

        # Remove a value from the stack and return
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size-=1
        return remove.value

# Driver code
if __name__=="__main__":
    stack=Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")

    for _ in range(1,6):
        remove = stack.pop()
        print(f"Pop:{remove}")
    print(f"Stack:{stack}")
