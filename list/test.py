#
#
# 
#  square of all odd numbers from range 1 to 10
# odd_square=[x**2 for x in range(1,11) if x%2==1]
# print(odd_square)


odd_square=[]
for x in range(1,11):
    if x%2==1:
        odd_square.append(x**2)
print(odd_square)

