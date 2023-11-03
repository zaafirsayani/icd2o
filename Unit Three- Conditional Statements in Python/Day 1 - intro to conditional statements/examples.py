# Check if a number is positive.
number = 89
if number > 0:
    print(f"{number} is positive")

if number <= 0:
    print(f"{number} is not positive")

# Determine if a person can vote (age 18 or older).
age = int(input("Please enter your age: "))

# if age >= 18:
#     not_eligable = ""
# if age < 18:
#     eligable = "not "

# print(f"You are eligable to {eligable}vote")
if age >= 18:
    print("This person is of age to vote") 

if age < 18:
    print("This person is not able to vote")

# Check if a string is empty.
str = input("Please enter a String: ")
if len(str) == 0:
    print("The string is empty")
if len(str) != 0:
    print("The string is not empty")
# Write a function that returns the maximum of two numbers.
def max_number(a, b):
    if a>b:
        return a
    
    return b

print(max_number(4,5))
print(max_number(14,5))


# Check if a user's input is equal to a secret password.
def password_checker(password, user_input):
    if password == user_input:
        return True
    
    return False

pwd = input("Password: ")
secret = "DFGHJGKHJGDF"
print(password_checker(secret,pwd))

# def password_checker(password, user_input):
#     if password == user_input:



# Write a function that checks if a number is within a specific range.(lower-upper inclusive)

def range_checker(num, lower, upper):
    if lower <= num <= upper:
        return True
    
    return False

a = int(input("Please enter a number between 1 and 10: "))
if (range_checker(a, 1, 10)):
    print("Good you listen to instructions!!")

if (range_checker(a, 1, 10)) == False :
    print("ARGHHHHH!!!!!!! I am not happy because you DONT LISTEN")

# Write a function that accepts a numberical grade and returns the Letter Grade
def grade_converter(grade):
    if grade >= 80:
        return "A"
    if grade >= 70:
        return "B"
    if grade >= 60:
        return "C"
    if grade >= 50:
        return "D"
    return "F"
