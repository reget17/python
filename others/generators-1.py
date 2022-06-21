def fib(number):
    num1 = 0
    num2 = 1
    
    for i in range(number):
        yield num1
        num1, num2 = num2, num1+num2

# def fib2(number):
#     num1 = 0
#     num2 = 1
#     list = []

#     for i in range(number):
#         if i == 0:
#             list.append(i)
#         elif i == 1: 
#             list.append(i)
#         else:
#             list.append(num1+num2)
#             num1, num2 = num2, num1+num2
#     return list

for i in fib(5):
    print(i)

# print(fib2(20))