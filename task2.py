#! python3
# Have the user input a number 
# Determine if the number is positive, negative or 0 
# 2 points

# Inputs:
# number

# Outputs:
# - "positive"
# - "negative"
# - "zero"
number=float(input("Input a number "))
if number>0:
    print("positive")
if number==0:
    print("zero")
if number<0:
    print("negative")
