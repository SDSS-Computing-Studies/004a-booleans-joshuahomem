#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# It is close enough if the expected length of the hypotenuse and the actual length 
# differ by no more than 2% 
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
a=input("enter short side 1 ")
b=input("enter short side 2 ")
c=input("enter hypotenuse ")
a=float(a)
b=float(b)
c=float(c)

side1=a**2
side2=b**2
side3=c**2
value1=side1+side2
number1=value1*0.02
range1=value1+number1
range2=value1-number1

if side3>range2 and side3<range1:
    print("that is a right triangle")



elif side3>side1+side2:
    print("that is an obuse triangle")
elif side3<side1+side2:
    print("that in an acute triangle")

