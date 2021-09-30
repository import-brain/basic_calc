import math

import sys

import time


# adding

def calculator():
    def add(x, y):
        return x + y

    # subtracting

    def subtract(x, y):
        return x - y

    # multiplying

    def multiply(x, y):
        return x * y

    # dividing

    def divide(x, y):
        return x / y

    # exponentiation

    def exponent(x, y):
        return x ** y

    # modulo/remainder/whatever you want to call it

    def modulo(x, y):
        return x % y

    # square root

    def sqrroot(x):
        return math.sqrt(x)

    # circumference

    def circumference(x):
        return pi * x

    # area of circle

    def circle_area(x):
        return pi * (x ** 2)

    # sin, cos, tan

    def sin(x):
        return math.sin(x)

    def cos(x):
        return math.cos(x)

    def tan(x):
        return math.tan(x)

    pi = 3.14

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
    print("9. area of circle")
    print("10. sine")
    print("11. cosine")
    print("12. tangent")

    # Making the calculator work

    while True:

        choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12): ")

        if choice == '7':
            number_sqr = float(input("Enter number:"))
            print("The square root of", number_sqr, "is", sqrroot(number_sqr))
            exit_flow()

        elif choice == '8':
            circle_diameter = float(input("Diameter of circle:"))
            print("A circle with diameter", circle_diameter, "has a circumference of", circumference(circle_diameter))
            exit_flow()

        elif choice == '9':
            circle_radius = float(input("Radius of circle:"))
            print("A circle with radius", circle_radius, "has an area of", circle_area(circle_radius))
            exit_flow()

        elif choice == '10':
            type_choice = rad_or_degree()
            x = float(input("Number to be sined: "))
            if type_choice == 0:
                print("The sine of ", x, " is ", round(sin(math.radians(x)), 3))
            elif type_choice == 1:
                print("The sine of ", x, " is ", round(sin(x), 3))
            exit_flow() 

        elif choice == '11':
            type_choice = rad_or_degree()
            x = float(input("Number to be cosined: "))
            if type_choice == 0:
                print("The cosine of ", x, " is ", round(cos(math.radians(x)), 3))
            elif type_choice == 1:
                print("The cosine of ", x, " is ", round(cos(x), 3))
            exit_flow()

        elif choice == '12':
            type_choice = rad_or_degree()
            x = float(input("Number to be tanned: "))
            if type_choice == 0:
                print("The tangent of ", x, " is ", round(tan(math.radians(x)), 3))
            elif type_choice == 1:
                print("The tangent of ", x, " is ", round(tan(x), 3))
            exit_flow()

        # todo: where cos(x) = 0, tan(x) is undefined: write logic to throw error for this

        elif choice in ('1', '2', '3', '4', '5', '6'):
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
                print("The remainder/modulo of", number_1, "and", number_2, "is", modulo(number_1, number_2))
            exit_flow()

        else:
            print("Invalid operation selected, please try again")
            time.sleep(2)
            calculator()


def exit_flow():
    exit_choice = input("Exit? Or perform another calculation? (Y for another calculation, N for exit) ")

    if exit_choice in ('y', 'Y'):
        calculator()
    elif exit_choice in ('N', 'n'):
        sys.exit()
    else:
        print("Invalid answer, please try again")
        time.sleep(2)
        exit_flow()

def rad_or_degree():
    rad_or_degree = input("Degrees or radians? Enter 0 for degrees, 1 for radians: ")

    if rad_or_degree != '1' and rad_or_degree != '0':
        print("Must select 1 or 0")
        time.sleep(2)
        rad_or_degree()
    elif rad_or_degree == '1':
        return 1
    elif rad_or_degree == '0':
        return 0



calculator()
exit_flow()
# :)