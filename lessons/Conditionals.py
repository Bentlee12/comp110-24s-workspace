"""Demonstrate Conditionals"""

user_input: str= input ("Pick a number:")
print(type(user_input))
print(user_input)
user_number: int=int(user_input)

# if user_number is less than 10, print "small"
if user_number < 10:
    print("small")
else: # user_number >=10
    print ("big")
    
    print (user_number)