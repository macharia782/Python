#Loops
#You also need to tell the loop where to stop.
#if you were to print a word 5 times
for i in range(2):
    print("Hello, World!")

#what about using a while loop
count = 0
while count < 3:
    print("Hello, World!")
    count += 1  # This will increment the count by 1 each time the loop runs

#for loop with fruits
fruits =["apple", "banana", "strawberry"]
for item in fruits:
    print(item)  # This will print each fruit in the list one by one


#when the number is known use for loop, when the number is unknown use while loop
#for: Known number of iterations
#while: Unknown number of iterations

#count the number of laps in a race and then quit when the laps are over
counter = 0
while counter < 3: #condition to check if the counter is less than 3
    print("the race is still on")
    counter += 1  # This will increment the counter by 1 each time the loop runs
else:
    print("the race is over")

#count through a range of number of students using a for loop
#make python_students a variable that counts through a range of numbers
python_students = range(1, 3)  # This will create a range of numbers from 1 to 2 (3 is exclusive)

for student in python_students: # This will iterate through each number in the range
    print("these are python students", student) 

#set the range within the for loop
for student in range(1, 3):  # Same output but different way of writing it
    print("these are python students", student)  

#added a step size to the range function
for student in range (1, 11, 3): #1 is the starting number, 11 is the stopping number (exclusive), and 3 is the step size
    print("Hello Student", student)  # This will print "Hello Student" followed by the numbers 1, 4, 7, and 10

#for Loop
#the format of a for loop structure:
# for variable in sequence:
#     block of code to be executed

#We use break in a loop to exit the loop when a certain condition is met. 
for student in range(10):
    if student == 3: #will not print 3 because the loop will skip it and continue to the next iteration
        continue
    if student == 5:
        break
    print (student)  # This will print numbers from 0 to 9, but will skip 3 and stop at 5