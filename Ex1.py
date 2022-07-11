

from itertools import product


def multiplication():
    num1 = int(input("Pick your first number: "))
    num2 = int(input("Pick your secound number: "))
    
    product = num1 * num2
    print("Your product is:", product)


multiplication()