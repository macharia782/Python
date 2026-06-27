#Functional Programming and Importance with python
#while for Unknown,  for for Known
#An app can store files in db or files
#The purpose and benefits of using functions in programming
#Functions in programming are blocks of code that encapsulates a specific task or related  group of tasks.
#Each function can be developed and tested independently, making the overall program more organized and easier to understand.
#In def greet():, greet is the function name.
def square(number):
    return number ** number
user_input = int(input("Enter a number to square: "))
result = square(user_input)
print("result is:", result)

#Function to add two number

def add(a, b):
    return a + b
result = add(3, 5)
print(result)

#One that performs all calculator mathematical functions):
def calculate():
    while True:
        try: #check for errors during input
            num1 = int(input("Enter a number: "))
            operator = input("Enter Operator:(=,-,*,/): ")
            num2 = int(input("Enter the second: "))
        except ValueError: #catch error if user inputs a string
            print("Invalid input, please enter a number")
            continue #to restart the loop

        if operator == "+":
            ans = num1 + num2
        elif operator == "-":
            ans = num1 - num2
        elif operator == "*":
            ans = num1 * num2
        elif operator == "/":
            if num2 == 0: # Prevents a crash if dividing by zero
                print("Error: Cannot divide by zero.\n")
                continue
            ans =  num1 / num2
        else:
            print("Invalid input")

        with open("my_calculator.txt" , "a") as file: 
            file.write(f"the first num user typed was {num1}, the second number the user types is {num2}.\n")
        return ans

result = calculate()
print("The result is: " , result)

#result = calulate(num1,num2, operator)
#print("Result is: ", result)

#REGISTRATION
def registration():
    first_name = input("Enter you first name:")
    last_name = input("Enter your last name")
    sex = input("Enter your sex: ")
    residence = input("Enter your residence:")
    send = input("Plese press S")
    
    if send.upper() == "S":
        registration()
        with open("registration.txt", "a"):
            file.write(f"{last_name}, {last_name}, {residence}")
    else:
        print("Registration is cancelled")
    print("Submitted successfully")

print(f"""
Dear {last_name}
It has been submitted
"""
    )

save = registration(first_name, last_name, sex, residence, send)
print("Message", save)
