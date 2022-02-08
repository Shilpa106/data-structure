# sum of digits of a number until sum becomes single digit


# if n<10
#   digSum(n)=n
# else
#   digSum(n)=Sum(digSum(n))

# M1
# ***********************************
# import math
# def digSum(n):
#     sum=0
#     while(n>0 or sum>9):
#         if(n==0):
#             n=sum
#             sum=0
#         sum+= n%10
#         n/=10
#     return sum

# # driver method
# n=1234
# print(digSum(n))

# **************************
# # M2
# def digSum(n):
#     if(n==0):
#         return 0
#     if(n%9==0):
#         return 9
#     else:
#         return(n%9)

# # driver program to test the above function
# n=9999
# print(digSum(n))

# /***/************************

# M3
# def getSum(n):
#     sum=0
#     while(n!=0):
#         sum=sum+int(n%10)
#         n=int(n/10)

#     return sum

# # driver code
# n=687
# print(getSum(n))

# ****************************

# # M4
# def sumDigits(no):
#     return 0 if no==0 else int(no%10)+sumDigits(int(no/10))

# # Driver code
# print(sumDigits(6874))

# ***********************************
# M5
# take ip as a string because of length issue for int

# def getSum(n):
#     # initializing sum to 0
#     sum=0
#     # traversing through string
#     for i in n:
#         # Converting char to int
#         sum=sum+int(i)

#     return sum

# n="123456789123456789123422"
# print(getSum(n))


# ******************
#sum of digits using Tail recursion
# M6

# def sum_of_digit(n, val):

#     if(n<10):
#         val=val+n
#         return val
    
#     return sum_of_digit(n // 10, (n%10) + val)

# # Driver code
# num=12345
# result=sum_of_digit(num, 0)
# print("Sum of digits is", result)

# /****************************************

# sum of digits in all numbers from 1 to n
# M1


def sumOfDigitsFrom1ToN(n):
    result=0
    for x in range(1, n+1):
        result=result+sumOfDigits(x)
    return result

def sumOfDigits(x):
    sum=0
    while(x!=0):
        sum=sum+x%10
        x=x//10
    return sum


n=328
print("sum of digits in numbers from 1 to", n, "is", sumOfDigitsFrom1ToN(n))


