
# This is is the none funcation based code 

# Here we ask the user to pick two numbers 
number_1 = int(input("First number: "));
number_2 = int(input("Second number: "));

# Here we made an if-else statemeant 
#   1. Checkes if the numbers multiplied are less then 1000 
#       if so, it will just just spit out the product, if not 
#       it will spit out the added value 
if(number_1 * number_2 <= 1000):
    print(number_1 * number_2);
else:
    print(number_1 + number_2);





# This is a funcation based code

#  Here we made a funcation 
def multiplication_or_sum():
    # Same as before, we ask the user for two imputs
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))

    # Here we made two varibles that do math opertions, one for addtion and one for multiplacation
    added = num1 + num2
    product = num1 * num2
    
    # Here we made an if-else statemeant that checks if the product is less then 1000 
    # and does the same as before. 
    if product <= 1000:
        print("Your product is:", product)

    else:
        print("Your number exceed 1000 when multiplied so it's added togther:", added)
        
        
# Here we're calling upon the funcation
multiplication_or_sum()





