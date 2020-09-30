#! python3

# Have the user enter in a sentence. 
# Check to see if the word "password" is located in the sentence

# Inputs:
# a sentence

# Outputs:
# "the sentence contains password"
# "the sentence does not contain password"
a=input("put in your scentence").strip()


if "password" in a:
    print("the scentence contains password")
else:
    print("the scentence does not contain password")
