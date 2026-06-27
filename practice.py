#Data types in Python
my_integer_var = 10
print(type(my_integer_var))  # <class 'int'>

my_float_var = 4.50
print(type(my_float_var))  # <class 'float'>

my_string_var = 'hello'
print(type(my_string_var))  # <class 'str'>

my_boolean_var = True
print(type(my_boolean_var))  # <class 'bool'>

my_set_var = {7, 'hello', 8.5}
print(type(my_set_var))  # <class 'set'>

my_dictionary_var = {'name': 'Alice', 'age': 25}
print(type(my_dictionary_var))  # <class 'dict'>

my_tuple_var = (7, 'hello', 8.5)
print(type(my_tuple_var))  # <class 'tuple'>

my_range_var = range(5)
print(type(my_range_var))  # <class 'range'>

my_list = [22, 'Hello world', 3.14, True]
print(type(my_list)) # <class 'list'>

my_none_var = None
print(type(my_none_var))  # <class 'NoneType'>

#There will be times in your program where you will need to verify that a particular variable is a specific type #before performing operations on it. This is where the isinstance() function comes in handy.

account_balance = '12'
print(isinstance(account_balance, int)) # False

#The built-in isinstance() function lets you check if a variable matches a specific data type. It takes in an object and the type you want to check it against, then returns a boolean

#The isinstance() function also allows you to check for multiple types at once.
account_balance = 12
print(isinstance(account_balance, (int, float))) # True

#Another example of isinstance() being used in a if statement
account_balance = 12

if isinstance(account_balance, (int, float)):
    print(f"Valid balance: ${account_balance:.2f}")
else:
    print("Error: Account balance must be a number.")


#Formatting rules to add specific number of decimal pointa
#The .2f part is a formatting specifier that means "format this number as a Float with exactly 2 decimal places."

balance = 12
print(f"${balance:.2f}")  
# Output: $12.00 (Adds trailing zeros)

pi = 3.14159
print(f"{pi:.2f}")       
# Output: 3.14 (Trims the excess decimals)

price = 10.567
print(f"${price:.2f}")    
# Output: $10.57 (Automatically rounds to the nearest cent)

# ,.2f – Adds commas as thousands separators and keeps 2 decimals (e.g., 12500 becomes 12,500.00
balance = 1250050.756 # A large account balance
 
# Format with thousands separators and 2 decimal places
formatted_balance = f"${balance:,.2f}"

print(formatted_balance) # Output: $1,250,050.76


#Checking Data Types
name = 'Alice'
print(name, type(name))

is_student = True
print(is_student, type(is_student))

age = 20
print(age, type(age))

score = 80.5
print(isinstance(score, int)) #returns false
print(score, type(score))

#Strings
#A normal string
ages = "one"
#A multi-line string
Aging = """this is a
multi-line string"""
print(Aging)

#Sometimes, you may need to check if a string contains one or more characters. For that, Python provides the in #operator, which returns a boolean that specifies whether the character or characters exist in the string or not.
my_name = "John"
print("John" in my_name) #true if John is in my_name
print("Joyce" in my_name)

#Indexing is getting the length of a string and working with the individual characters in the string
my_str = 'Hello world'
print(len(my_str))  # 11

#To access a character by its index, you use square brackets ([]) with the index of the character you want to access inside.
print(my_str[0])  # H
print(my_str[6])  # w
#Negative indexing is also allowed, so you can get the last character of any string with -1
print(my_str[-1])  # d
print(my_str[-2]) # l

#CONCATENATION
#In Python, you can combine multiple strings together with the plus (+) operator. This process is called string concatenation.
my_str = "Good"
my_str_1 = "Morning"

print(my_str + " " + my_str_1)

my_name = "James"
age = 21

my_name_and_age = my_name + " " +str(age)
print(my_name_and_age)  #James 21

#You can also use the augmented assignment operator for concatenation. 
#This is represented by a plus and equals sign (+=), and performs both concatenation and assignment in one step.
a_name = 'John Doe '
age = 26

name_and_age = a_name  # Start with the name
name_and_age += str(age)  # Append the age as string

print(name_and_age)  # John Doe 26


#STRING INTERPOLATION
#The process of inserting variables and expressions into a string is called string interpolation.
#Python has a category of string called f-strings (short for formatted string literals),
# which allows you to handle interpolation with a compact and readable syntax.
num1 = 5
num2 = 10
print(f"The sum of {num1} and {num2} is {num1 + num2}")

#String slicing lets you extract a portion of a string or work with only a specific part of it. 
greeting = 'Hello world'
print(greeting[1:4]) # ell
#Apart from the start and stop indices, there's also an optional step parameter, 
#which is used to specify the increment between each index in the slice.
#string[start:stop:step]
print(greeting[0:11:2])  # Hlowrd
#A helpful trick you can do with the step parameter is to reverse a string by setting step to -1, 
#and leaving start and stop blank:
print(greeting[::-1]) # dlrow olleH


#string methods
uppercase_my_str = my_str.upper()
print(uppercase_my_str) #make them uppercase

replaced_my_str = my_str.replace('Good', 'hi')
print(replaced_my_str)  #replace the words
 