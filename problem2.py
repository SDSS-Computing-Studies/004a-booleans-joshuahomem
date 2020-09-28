#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"

a=input("enter in your number")
a=float(a)
b=int(a)

if b==a:
    print("the number is an integer")
else:
    print("the number is not an integer")
