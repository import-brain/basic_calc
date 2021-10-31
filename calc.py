import math
import sys
import time

class NotSupportedVersionException(BaseException):
    def __init__(self):
        pass
#all helper functions
def versionCheck():
    MiniumPythonVersion=(3, 10)    
    CurrentVersion=(sys.version_info.major, sys.version_info.minor)
    if CurrentVersion >= MiniumPythonVersion :
        pass
    else :
        print("Due to code used in this program, any version below 3.10 is not able to run this program, goto https://docs.python.org/3/whatsnew/3.10.html for more information.\n current version: "+sys.version)
        raise NotSupportedVersionException

def safeConvert(value : str, defaultValue : str, function):
    try:
        return function(value)
    except ValueError:
        return defaultValue

def exit_flow(printed_message: str):
    
    if printed_message != "15": # if user chooses to read calculations from storage, don't prompt user to save calculation
        save_choice = input("Do you wish to save your calculation to local storage? (Y for yes, N for no) ")

        if save_choice in ('y', 'Y', 'yes', 'Yes'):
            write_file(printed_message)
            time.sleep(1)
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
        exit_flow("x")

def write_file(what_to_write: str):
        file_name = str(input("Desired file name: ") + ".txt")
        try: # try to create file, if file already exists (IOError), go into append mode, and if no error, also go into append mode
            save_file = open(file_name, 'x')
        except IOError:
            with open(file_name, mode='a') as file_object:
                print(what_to_write, file=file_object)
        else:
            with open(file_name, mode='a') as file_object:
                print(what_to_write, file=file_object)
        print("Calculation saved to ", file_name)

def read_file():
    file_name = str(input("Which storage file would you like to read?") + ".txt")
    try:
        with open(file_name, mode='r') as file_object:
            # todo: implement ability for user to pick how many previous calculations to print, error handling for if user picks more lines than the file contains
            for line in file_object:
                print(line, end = '')
    # if file not found, return error
    except FileNotFoundError:
        print("File not found, please try again")
        time.sleep(1)
        read_file()

    


# adding

def calculator():
    def safeInputSingleValue(PromptMessage : str) -> float:
        Value = None
        while Value == None:
            Value=safeConvert(input(PromptMessage), None, float)
            
        return Value
    
    def runAndRound2Value(x : float, y : float, func) -> float: 
        return round(func(x, y),int(input("Rounding place: ")))
    
    def runAndRound1Value(x : float, func) -> float: 
        return round(func(x),int(input("Rounding place: ")))
        
    def add(x : float, y : float) -> float:
        return x + y

    # subtracting

    def subtract(x : float, y : float) -> float:
        return x - y

    # multiplying

    def multiply(x : float, y : float) -> float:
        return x * y

    # dividing

    def divide(x : float, y : float) -> float:
        return x / y

    # exponentiation

    def exponent(x : float, y : float) -> float:
        return x ** y

    # modulo/remainder/whatever you want to call it

    def modulo(x : float, y : float) -> float:
        return x % y

    # square root

    def sqrroot(x : float) -> float:
        return exponent(x, 2)

    # circumference

    def circumference(x : float) -> float:
        return math.pi * x

    # area of circle

    def circle_area(x : float) -> float:
        return math.pi * (x ** 2)

    # sin, cos, tan

    def sin(x : float) -> float:
        return math.sin(x)

    def cos(x : float) -> float:
        return math.cos(x)

    def tan(x : float) -> float:
        return math.tan(x)

    def rad(x : float) -> float:
        return math.radians(x)

    def deg(x : float) -> float:
        return math.degrees(x)

    def rad_or_degree() -> int: # rad or degree choice picker function
        Vrad_or_degree = None
        while Vrad_or_degree == None:
            Vrad_or_degree = safeConvert(input("Degrees or radians? Enter 0 for degrees, 1 for radians: "), None, int)
            if Vrad_or_degree == 1 or Vrad_or_degree == 0:
                return Vrad_or_degree
                break
            else:
                print("Must select 1 or 0")
                time.sleep(2)

    # User prompt to select operation

    print("Select an operation")
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
    print("15. read previous calculations")
    print("-E to exit")

    # Making the calculator work

    while True:
        # todo: fix spacing issues in output to file
        # For every choice, execute operations based on user input

        choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13/14/15): ")
        if choice.__eq__("-E"):
            sys.exit(0)
        
        if choice in ('1', '2', '3', '4', '5', '6'):
            number_1 = None
            number_2 = None
            
            while number_1 == None or number_2 == None :
                print("repeat if bad value is entered (bad values are anything that is not a number)")
                number_1 = safeConvert(input("Enter first number: "), None, float)
                number_2 = safeConvert(input("Enter second number: "), None, float)
            
            match choice:
                case '1':
                    print(number_1, "+", number_2, "=", runAndRound2Value(number_1, number_2, add))
                    exit_flow(str(number_1) + "+" + str(number_2) + "=" + str(add(number_1, number_2)))
                
                case '2':
                    print(number_1, "-", number_2, "=", runAndRound2Value(number_1, number_2, subtract))
                    exit_flow(str(number_1) + "-" + str(number_2) + "=" + str(subtract(number_1, number_2)))

                case '3':
                    print(number_1, "*", number_2, "=", runAndRound2Value(number_1, number_2, multiply))
                    exit_flow(str(number_1) + "*" + str(number_2) + "=" + str(multiply(number_1, number_2)))

                case '4':
                    if number_2 == 0: # if user attempts to input by 0, return error message
                        print("Oops! Numbers cannot be divided by 0")
                    else:
                        print(number_1, "/", number_2, "=", runAndRound2Value(number_1, number_2, divide))
                        exit_flow(str(number_1) + "/" + str(number_2) + "=" + str(divide(number_1, number_2)))
    
                case '5':
                    print(number_1, "to the power of", number_2, "=", runAndRound2Value(number_1, number_2, exponent))
                    exit_flow(str(number_1) + "to the power of" + str(number_2) + "=" + str(exponent(number_1, number_2)))
                    
                case '6':
                    if number_2 == 0: # if user attempts to input by 0, return error message
                        print("Oops! Numbers cannot be divided by 0")
                    else:
                        print(number_1, "/", number_2, "=", runAndRound2Value(number_1, number_2, modulo))
                        exit_flow(str(number_1) + "/" + str(number_2) + "=" + str(modulo(number_1, number_2)))
                        
        else: 
            number = safeInputSingleValue("Enter Number")
            match choice:
                case '7':
                    print("The square root of", number, "is", runAndRound1Value(number, sqrroot))
                    exit_flow("The square root of" + str(number) + "is" + str(sqrroot(number)))
        
                case '8':
                    print("A circle with diameter", number, "has a circumference of", runAndRound1Value(number, circumference))
                    exit_flow("A circle with diameter" + str(number) + "has a circumference of" + str(circumference(number)))
        
                case '9':
                    print("A circle with radius", number, "has an area of", runAndRound1Value(number, circle_area))
                    exit_flow("A circle with radius" + str(number) + "has an area of" + str(circle_area(number)))
        
                case '10':
                    match rad_or_degree():
                        case 0:
                            print("The sine of ", number, " degrees is ", runAndRound1Value(math.radians(number), sin))
                            exit_flow("The sine of " + str(number) + " degrees is " + str(round(sin(math.radians(number)), 3)))
                        case 1:
                            print("The sine of ", number, " radians is ", runAndRound1Value(number, sin))
                            exit_flow("The sine of " + str(number) + " radians is " + str(round(sin(number), 3))) 
        
                case '11':
                    match rad_or_degree:
                        case 0:
                            print("The cosine of ", number, " degrees is ", round(cos(math.radians(number)), 3))
                            exit_flow("The cosine of " + str(number) + " degrees is " + str(round(cos(math.radians(number)), 3)))
                        case 1:
                            print("The cosine of ", number, " radians is ", round(cos(number), 3))
                            exit_flow("The cosine of " + str(number) + " radians is " + str(round(cos(number), 3)))
        
                case '12':
                    type_choice = rad_or_degree()
                    if cos(math.radians(number) if type_choice==0 else number) == 0:
                        print("Tangent of ", number, "degrees" if type_choice==0 else "radians", "is undefined")
                        exit_flow("Tangent of " + str(number) + ("degrees" if type_choice==0 else "radians") + " is undefined")
                    
                    match type_choice:
                        case 0:
                                print("The tangent of ", number, " degrees is ", round(tan(math.radians(number)), 3))
                                exit_flow("The tangent of " + str(number) + " degrees is " + str(round(tan(math.radians(number)), 3)))
                        case 1:
                                print("The tangent of ", number, " radians is ", round(tan(number), 3))
                                exit_flow("The tangent of " + str(number) + " radians is " + str(round(tan(number), 3)))
        
                case '13':
                    print(number, " degrees converted to radians is", rad((number)), " radians ")
                    exit_flow(str(number) + " degrees converted to radians is " + str(rad((number))) + " radians ")
        
                case '14':
                    print(number, " radians converted to degrees is", deg(number / 3.14 * math.pi), " degrees ")
                    exit_flow(str(number) + " radians converted to degrees is " + str(deg(number / 3.14 * math.pi)) + " degrees ")
                case '15':
                    read_file()
                    exit_flow("15")        
                
                case _: #  if operation choice is not within the range of 1-15, return error message to user and prompt them again
                    print("Invalid operation selected, please try again")
                    time.sleep(2)
         
versionCheck()       
calculator()
# :)