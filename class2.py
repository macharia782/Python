a = "4"
b = 4
# cannot concatenate due to type mismatch
# result = a + b
result = a + str(b)  # Convert b to string before concatenation
print(result)

c = "4"
d = str(4)
# Now both c and d are strings, so concatenation works
result2 = c + d
print(result2)


print(type(a))  # This will print <class 'str'>) 
type (a)  # This needs the print in order to display <class 'str'>) 

#Arithmetic operators
print(10 // 3)  # This will print 3, which is the floor division result of 10 divided by 3
print(10 / 3)  # This will print 3.3333333333333335, which is the result of 10 divided by 3
print(10 % 3)  # This will print 1, which is the remainder of 10 divided by 3
print(10 ** 3)  # This will print 1000, which is 10 raised to the power of 3

print(17 // 5)  # This will print 3, which is the floor division result of 17 divided by 5
print(17 / 5)  # This will print 3.4, which is the
print(17 % 5)  # This will print 2, which is the remainder of 17 divided by 5
print(17 + 5)  # This will print 22, which is the sum of 17 and 5
print(17 - 5)  # This will print 12, which is the difference of 17 and 5
print(17 * 5)  # This will print 85, which is the product of 17 and 5    

#Arithmetic operations with variables
num1 = 10
num2 = 2
print(num1 + num2)  # This will print 12, which is the sum of num1 and num2
print(num1 - num2)  # This will print 8, which is the difference of num1 and num2
print(num1 * num2)  # This will print 20, which is the product of num1 and num2
print(num1 / num2)  # This will print 5.0, which is the result of num1 divided by num2
print(num1 // num2)  # This will print 5, which is the floor division result of num1 divided by num2
print(num1 % num2)  # This will print 0, which is the remainder of num1 divided by num2
print(num1 ** num2)  # This will print 100, which is num1 raised to the power of num2
