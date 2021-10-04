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

    def rad(x):
        return math.radians(x)

    def deg(x):
        return math.degrees(x)

    def rad_or_degree(): # rad or degree choice picker function
        rad_or_degree = input("Degrees or radians? Enter 0 for degrees, 1 for radians: ")

        if rad_or_degree != '1' and rad_or_degree != '0':
            print("Must select 1 or 0")
            time.sleep(2)
            rad_or_degree()
        elif rad_or_degree == '1':
            return 1
        elif rad_or_degree == '0':
            return 0

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
    print("13. convert degrees to radians")
    print("14. convert radians to degrees")

    # Making the calculator work

    while True:

        # For every choice, execute operations based on user input

        choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13/14): ")

        if choice == '7':
            number_sqr = float(input("Enter number:"))
            print("The square root of", number_sqr, "is", sqrroot(number_sqr))
            exit_flow("The square root of" + number_sqr + "is" + sqrroot(number_sqr))

        elif choice == '8':
            circle_diameter = float(input("Diameter of circle:"))
            print("A circle with diameter", circle_diameter, "has a circumference of", circumference(circle_diameter))
            exit_flow("A circle with diameter" + circle_diameter + "has a circumference of" + circumference(circle_diameter))

        elif choice == '9':
            circle_radius = float(input("Radius of circle:"))
            print("A circle with radius", circle_radius, "has an area of", circle_area(circle_radius))
            exit_flow("A circle with radius" + circle_radius + "has an area of" + circle_area(circle_radius))

        elif choice == '10':
            type_choice = rad_or_degree()
            x = float(input("Number to be sined: "))
            if type_choice == 0:
                print("The sine of ", x, " degrees is ", round(sin(math.radians(x)), 3))
                exit_flow("The sine of " + x + " degrees is " + round(sin(math.radians(x)), 3))
            elif type_choice == 1:
                print("The sine of ", x, " radians is ", round(sin(x), 3))
                exit_flow("The sine of " + x + " radians is " + round(sin(x), 3)) 

        elif choice == '11':
            type_choice = rad_or_degree()
            x = float(input("Number to be cosined: "))
            if type_choice == 0:
                print("The cosine of ", x, " degrees is ", round(cos(math.radians(x)), 3))
                exit_flow("The cosine of " + x + " degrees is " + round(cos(math.radians(x)), 3))
            elif type_choice == 1:
                print("The cosine of ", x, " radians is ", round(cos(x), 3))
                exit_flow("The cosine of " + x + " radians is " + round(cos(x), 3))

        elif choice == '12':
            type_choice = rad_or_degree()
            x = float(input("Number to be tanned: "))
            
            if type_choice == 0:
                if cos(math.radians(x)) == 0:
                    print("Tangent of ", x, " degrees is undefined")
                    exit_flow("Tangent of " + x + " degrees is undefined")
                else:
                    print("The tangent of ", x, " degrees is ", round(tan(math.radians(x)), 3))
                    exit_flow("The tangent of " + x + " degrees is " + round(tan(math.radians(x)), 3))
            elif type_choice == 1:
                if cos(x) == 0:
                    print("Tangent of ", x, " radians is undefined")
                    exit_flow("Tangent of " + x + " radians is undefined")
                else:
                    print("The tangent of ", x, " radians is ", round(tan(x), 3))
                    exit_flow("The tangent of " + x + " radians is " + round(tan(x), 3))

        elif choice == '13':
            measure = float(input("Degree measure to be converted to radians: "))
            print(measure, " degrees converted to radians is", rad((measure)), " radians ")
            exit_flow(measure + " degrees converted to radians is" + rad((measure)) + " radians ")

        elif choice == '14':
            measure = float(input("Radian measure to be converted to degrees: "))
            print(measure, " radians converted to degrees is", deg(measure / 3.14 * math.pi), " degrees ")
            exit_flow(measure + " radians converted to degrees is" + deg(measure / 3.14 * math.pi) + " degrees ")

        elif choice in ('1', '2', '3', '4', '5', '6'):
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))

            if choice == '1':
                print(number_1, "+", number_2, "=", add(number_1, number_2))
                exit_flow(number_1 + "+" + number_2 + "=" + add(number_1, number_2))

            elif choice == '2':
                print(number_1, "-", number_2, "=", subtract(number_1, number_2))
                exit_flow(number_1 + "-" + number_2 + "=" + subtract(number_1, number_2))

            elif choice == '3':
                print(number_1, "*", number_2, "=", multiply(number_1, number_2))
                exit_flow(number_1 + "*" + number_2 + "=" + multiply(number_1, number_2))

            elif choice == '4':
                try: # if user attempts to divide by 0, return error message
                    x = divide(number_1, number_2)
                except ZeroDivisionError:
                    print("Oops! Numbers cannot be divided by 0")
                else:
                    print(number_1, "/", number_2, "=", divide(number_1, number_2))
                    exit_flow(number_1 + "/" + number_2 + "=" + divide(number_1, number_2))

            elif choice == '5':
                print(number_1, "to the power of", number_2, "=", exponent(number_1, number_2))
                exit_flow(number_1 + "to the power of" + number_2 + "=" + exponent(number_1, number_2))
            elif choice == '6':
                try: # if user attempts to divide by 0, return error message
                    x = modulo(number_1, number_2)
                except ZeroDivisionError:
                    print("Oops! Numbers cannot be divided by 0")
                else:
                    print("The remainder/modulo of", number_1, "and", number_2, "is", modulo(number_1, number_2))
                    exit_flow("The remainder/modulo of" + number_1 + "and" + number_2 + "is" + modulo(number_1, number_2))

        else: #  if operation choice is not within the range of 1-14, return error message to user and prompt them again
            print("Invalid operation selected, please try again")
            time.sleep(2)
            calculator()


def exit_flow(printed_message: str):
    save_choice = input("Do you wish to save your calculation to local storage? (Y for yes, N for no) ")

    if save_choice in ('y', 'Y', 'yes', 'Yes'):
        write_file(printed_message)
    elif save_choice in ('n', 'N', 'no', 'No'):
        pass
    
    exit_choice = input("Exit? Or perform another calculation? (Y for another calculation, N for exit) ")

    if exit_choice in ('y', 'Y', 'yes', 'Yes'):
        calculator()
    elif exit_choice in ('N', 'n', 'No', 'no'):
        sys.exit()
    else:
        print("Invalid answer, please try again")
        time.sleep(2)
        exit_flow()

def write_file(what_to_write: str):
    try: # try to create file, if file already exists (IOError), go into append mode, and if no error, also go into append mode
        save_file = open('calculations.txt', 'x')
    except IOError:
        with open('calculations.txt', mode='a') as file_object:
            print(what_to_write, file=calculations.txt)
    else:
        with open('calculations.txt', mode='a') as file_object:
            print(what_to_write, file=calculations.txt)

def read_file():
    with open('calculations.txt', mode='r') as file_object:
        # todo: implement ability for user to pick how many previous calculations to print, error handling for if user picks more lines than the file contains
        for line in file_object:
            print(line, end = '')

    

calculator()
# :)