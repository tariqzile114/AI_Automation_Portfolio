fav_color = "Green"
goal_salary = 10_000
is_learning_python = True

print(fav_color)
print(goal_salary)
print(is_learning_python)

print("My favorite color is", fav_color, "I want to earn", goal_salary, "and learning Python is", is_learning_python)
# Use f_String
print(f"My Favorite color is {fav_color}, I want to earn {goal_salary}, and learning Python is {is_learning_python}.")

#create variable, convert it to hours and print.
minutes = 120
hours = minutes / 60
print("Hours:", hours)

#Create a number and convert it to a string and print "The number is ____"
number = 120
conv_to_String ="120"
print("The number is", conv_to_String) # Wrong

number1 = 125
conv_to_String =str(number1)
print("The number is", conv_to_String)

print(f"The number is {number1}")

# Variable Creation and Printing

name = "Crystal"
age = 23
fav_num = 4

print(name + " " + str(age) + " " + str(fav_num))

print(f"My name is {name}, I am {age} years old, and my favorite number is {fav_num}")

# Arithmetic Operations
num1 = 3
num2 = 4
num1 += 1

print(num1 + num2)
print(num1 - num2)
print(num1 % num2)
print(num1 * num2)
print(num1 / num2)
print(num1)

# String Manipulation

first_name = "Carol"
last_name = "Casey"
# concatenation
print("Full name",  first_name + " " + last_name)
# f-string
print(f"My full Name is {first_name} {last_name}")

sentence = "Python is fun"
#print the length of the string
string_length = len(sentence)
print(string_length)

# print string in uppercase
str_upcase = sentence.upper()
print(str_upcase)

# print string in lowercase
str_locase = sentence.lower()
print(str_locase)

# .format() method
print("My first name is {} and last name {}.".format(first_name, last_name))

minutes = 250

# Convert to hours (float)
hours_float = minutes / 60

# Convert to integer hours (truncating the decimal part)
hours_integer = int(hours_float)

print(f"Minutes: {minutes}")
print(f"Hours (float): {hours_float}")
print(f"Hours (integer): {hours_integer}")

#Create a variable num = 500 
#Convert it to a string and print "The number is 500"

num = 500
print("The number is",str(num))

#Create a string variable str_num = "1000"
#Convert it to an integer and print its double

str_num = "1000"
int_num = int(str_num)
print (str_num)
double_num = int_num * 2
print(double_num)

# Boolean and Conditional Practice
# Create a boolean variable is_learning = True
# Create a number variable score = 85

is_learning = True
score = 85

print(f"Learning python is {is_learning} and my score is {score}")

# Add conditional

if score > 90:
  print("Excellent!")
else:
  print("Keep practicing!")
