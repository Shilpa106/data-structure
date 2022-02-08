# # implementation of stack using array

# from sys import maxsize
# # function to create a stack. It initializes size of stack as 0
# def createStack():
#     stack=[]
#     return stack

# # stack is empty when stack size is 0
# def isEmpty(stack):
#     return len(stack)==0

# # function to add an item to stack. It increases size by 1
# def push(stack, item):
#     stack.append(item)
#     print(item + "pushed to stack")

# # Function to remove an item from stack. It decreases size by 1
# def pop(stack):
#     if(isEmpty(stack)):
#         return str(-maxsize-1)

#     return stack.pop()


# def peek(stack):
#     if(isEmpty(stack)):
#         return str(-maxsize-1)
#     return stack[len(stack)-1]


# # driver program to taest above functions
# stack=createStack()
# push(stack, str(10))
# push(stack, str(20))
# push(stack, str(30))
# print(pop(stack)+"popped from stack")


# **************************************************************

# from sys import implementation


# # implementation of stack using linked list
# class StackNode:
#     # Constructor to initialize a node
#     def __init__(self, data):
#         self.data=data
#         self.next=None

# class Stack:
#     # constructor to initialize the root of linked list
#     def __init__(self):
#         self.root=None

#     def isEmpty(self):
#         return True if self.root is None else False

#     def push(self, data):
#         newNode=StackNode(data)
#         newNode.next = self.root
#         self.root=newNode
#         print("% d pushed to stack" % (data))

#     def pop(self):
#         if (self.isEmpty()):
#             return float("-inf")
#         temp = self.root
#         self.root=self.root.next
#         popped=temp.data
#         return popped

#     def peek(self):
#         if self.isEmpty():
#             return float("-inf")
#         return self.root.data


# # Driver code
# stack=Stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)

# print("%d popped from stack " % (stack.pop()))
# print("Top element is % d " % (stack.peek()))


# *******************************************************
# Infix to Postfix expression

# Class to convert the expression
from urllib3 import Retry


class Conversion:

    # constructor to initialize the class variables
    def __init__(self,capacity):
        self.top=-1
        self.capacity=capacity
        # this array is used a stack
        self.array=[]
        # precedence setting
        self.output=[]
        self.precedence={'+':1, '-':1, '*':2, '/':2,'^':3}

# check if the stack is empty
    def isEmpty(self):
        return True if self.top==-1 else False

    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]

    # pop the element from the stack
    def pop(self):
        if not self.isEmpty():
            self.top-=1
            return self.array.pop()
        else:
            return "$"

    # push the element to the stack
    def push(self, op):
        self.top+=1
        self.array.append(op)

    # A utility function to check is the given character is operand
    def isOperand(self, ch):
        return ch.isalpha()

    # check if the precedence of operator is strictly less than top of stack or not
    def notGreater(self, i):
        try:
            a=self.precedence[i]
            b=self.precedence[self.peek()]
            return True if a <=b else False
        except KeyError:
            return False


    # the main function that converts given infix expression to postfix expression
    def infixToPostfix(self, exp):
        # Iterate over the expression for conversion
        for i in exp:
            # if the character is an operand ,add it to op
            if self.isOperand(i):
                self.output.append(i)

            # if the character is an '(', push it to stack
            elif i == '(':
                self.push(i)

            # if the scanned character is an ')', pop and output from the stack until and '(' is found
            elif i == ')':
                while((not self.isEmpty()) and self.peek()!='('):
                    a=self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek()!='('):
                    return -1
                else:
                    self.pop()

            # An operator is encountered
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)


# pop all the operator from the stack
        while not self.isEmpty():
            self.output.append(self.pop())

        print("".join(self.output))

# Driver program to test above function
exp="a+b*(c^d-e)^(f+g*h)-i"
obj=Conversion(len(exp))
obj.infixToPostfix(exp)

