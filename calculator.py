import math


# adding

def add(x,y):
    return x + y

# subtracting

def subtract(x,y):
    return x - y

# multiplying

def multiply(x,y):
    return x * y

# dividng

def divide(x,y):
    return x / y

# exponentiation

def exponent(x,y):
    return x ** y

# modulo/remainder/whatever you want to call it

def modulo(x,y):
    return x % y

# square root

def sqrroot(x):
    return math.sqrt(x)

# circumference

def circumference(x):
    return (math.pi * 2 * x)




# User prompt to select operation

print("Select operation")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")
print("5. exponent")
print("6. modulo/remainder")
print("7. square root")
print("8. circumference")

# Making the calculator work

while True:

    choice = input("Enter choice(1/2/3/4/5/6/7/8): ")

    if choice in ('7'):
        number_sqr = float(input("Enter number:"))
        print("The square root of", number_sqr, "is", sqrroot(number_sqr))
        break

    if choice in ('8'):
        circle_radius = float(input("Radius of circle:"))
        print("A circle with radius", circle_radius, "has a circumference of", circumference(circle_radius))
        break

    if choice in ('1', '2', '3', '4', '5', '6'):
        number_1 = float(input("Enter first number: "))
        number_2 = float(input("Enter second number: "))

        if choice == '1':
            print(number_1, "+", number_2, "=", add(number_1, number_2))

        elif choice == '2':
            print(number_1, "-", number_2, "=", subtract(number_1, number_2))

        elif choice == '3':
            print(number_1, "*", number_2, "=", multiply(number_1, number_2))

        elif choice == '4':
            print(number_1, "/", number_2, "=", divide(number_1, number_2))

        elif choice == '5':
            print(number_1, "to the power of", number_2, "=", exponent(number_1, number_2))

        elif choice == '6':
            print("The remainder/modulo of", number_1, "and", number_2, "is", modulo(number_1,number_2))
        break
else:
    print("Invalid input: select operation")

# :)

input("Thank you for using my calculator! Press enter to exit")
