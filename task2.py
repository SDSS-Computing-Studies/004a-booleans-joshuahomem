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

a=input("enter in number")
a=float(a)

if a==0:
    print("Zero")

if a>0:
    print("posotive")

if a<0:
    print("negative")
