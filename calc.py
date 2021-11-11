import math
import sys
import time

#all helper functions
def versionCheck() -> bool:
    """return true if it can use match case else false"""
    MinimumPythonVersion=(3, 10)    
    CurrentVersion=(sys.version_info.major, sys.version_info.minor)
    if CurrentVersion >= MinimumPythonVersion :
        return True
    else :
        return False

def safeConvert(value : str, defaultValue : str, function):
    try:
        return function(value)
    except ValueError:
        return defaultValue

#DONOT port exit_flow!
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
        file_name = str(input("Desired file name: (-E to cancel)") + ".txt")
        if file_name.__eq__("-E"):
            return
            
        try: # try to create file, if file already exists (IOError), go into append mode, and if no error, also go into append mode
            save_file = open(file_name, 'x')  # @UnusedVariable
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
    
    pass


def calculator():
    def safeInputSingleValue(PromptMessage : str) -> float:
        Value = None
        while Value == None:
            Value=safeConvert(input(PromptMessage), None, float)
            
        return Value
    
    def safeInputDoubleValue(PromptMessage1 : str, PromptMessage2 : str) -> tuple:
        number_1 = None
        number_2 = None
        
        while number_1 == None or number_2 == None :
            print("repeat if bad value is entered (bad values are anything that is not a number)")
            number_1 = safeConvert(input(PromptMessage1), None, float)
            number_2 = safeConvert(input(PromptMessage2), None, float)
        
        return (number_1,number_2)
    
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

    def rad_or_degree() -> bool: # rad or degree choice picker function
        Vrad_or_degree = safeInputSingleValue("Degrees or radians? Enter 0 for degrees, 1 for radians: ")
        if Vrad_or_degree == 1 or Vrad_or_degree == 0:
            return True if Vrad_or_degree==1 else False
        else:
            print("Must select 1 or 0")
            time.sleep(2)
            
    def addFunction(inputs : tuple):
        print(inputs[0], "+", inputs[1], "=", runAndRound2Value(inputs[0], inputs[1], add))
        exit_flow(str(inputs[0]) + "+" + str(inputs[1]) + "=" + str(add(inputs[1], inputs[2])))
    
    def subtFunction(inputs : tuple):
        print(inputs[0], "-", inputs[1], "=", runAndRound2Value(inputs[0], inputs[1], subtract))
        exit_flow(str(inputs[0]) + "-" + str(inputs[1]) + "=" + str(subtract(inputs[0], inputs[1])))
        
    def multFunction(inputs : tuple):
        print(inputs[0], "*", inputs[1], "=", runAndRound2Value(inputs[0], inputs[1], multiply))
        exit_flow(str(inputs[0]) + "*" + str(inputs[1]) + "=" + str(multiply(inputs[0], inputs[1])))
    
    def divFunction(inputs : tuple):
        if inputs[1] == 0: # if user attempts to input by 0, return error message
            print("Oops! Numbers cannot be divided by 0")
        else:
            print(inputs[0], "/", inputs[1], "=", runAndRound2Value(inputs[0], inputs[1], divide))
            exit_flow(str(inputs[0]) + "/" + str(inputs[1]) + "=" + str(divide(inputs[0], inputs[1])))
    
    def sqrFuction(inputs : tuple):
        print(inputs[0], "to the power of", inputs[1], "=", runAndRound2Value(inputs[0], inputs[1], exponent))
        exit_flow(str(inputs[0]) + "to the power of" + str(inputs[1]) + "=" + str(exponent(inputs[0], inputs[1])))
    
    def modFunction(inputs : tuple):
        if inputs[1] == 0: # if user attempts to input by 0, return error message
            print("Oops! Numbers cannot be divided by 0")
        else:
            print(inputs[0], "/", inputs[1], "=", runAndRound2Value(inputs[0], inputs[1], modulo))
            exit_flow(str(inputs[0]) + "/" + str(inputs[1]) + "=" + str(modulo(inputs[0], inputs[1])))
    
    def sqrtFunction(inputValue : float):
        print("The square root of", inputValue, "is", runAndRound1Value(inputValue, sqrroot))
        exit_flow("The square root of" + str(inputValue) + "is" + str(sqrroot(inputValue)))
    
    def circFunction(inputValue : float):
        print("A circle with diameter", inputValue, "has a circumference of", runAndRound1Value(inputValue, circumference))
        exit_flow("A circle with diameter" + str(inputValue) + "has a circumference of" + str(circumference(inputValue)))
    
    def ciraFunction(inputValue : float):
        print("A circle with radius", inputValue, "has an area of", runAndRound1Value(inputValue, circle_area))
        exit_flow("A circle with radius" + str(inputValue) + "has an area of" + str(circle_area(inputValue)))
    
    def sinFunction(inputValue : float):
        if rad_or_degree():
            print("The sine of ", inputValue, " degrees is ", runAndRound1Value(math.radians(inputValue), sin))
            exit_flow("The sine of " + str(inputValue) + " degrees is " + str(round(sin(math.radians(inputValue)), 3)))
        else:
            print("The sine of ", inputValue, " radians is ", runAndRound1Value(inputValue, sin))
            exit_flow("The sine of " + str(inputValue) + " radians is " + str(round(sin(inputValue), 3)))
    
    def cosFunction(inputValue : float):
        if rad_or_degree():
            print("The cosine of ", inputValue, " degrees is ", round(cos(math.radians(inputValue)), 3))
            exit_flow("The cosine of " + str(inputValue) + " degrees is " + str(round(cos(math.radians(inputValue)), 3)))
        else:
            print("The cosine of ", inputValue, " radians is ", round(cos(inputValue), 3))
            exit_flow("The cosine of " + str(inputValue) + " radians is " + str(round(cos(inputValue), 3)))
    
    def tanFunction(inputValue : float):
        type_choice = rad_or_degree()
        if cos(math.radians(inputValue) if not(type_choice) else inputValue) == 0:
            print("Tangent of ", inputValue, "degrees" if type_choice==0 else "radians", "is undefined")
            exit_flow("Tangent of " + str(inputValue) + ("degrees" if type_choice==0 else "radians") + " is undefined")
                     
        if type_choice:
            print("The tangent of ", inputValue, " degrees is ", round(tan(math.radians(inputValue)), 3))
            exit_flow("The tangent of " + str(inputValue) + " degrees is " + str(round(tan(math.radians(inputValue)), 3)))
        else:
            print("The tangent of ", inputValue, " radians is ", round(tan(inputValue), 3))
            exit_flow("The tangent of " + str(inputValue) + " radians is " + str(round(tan(inputValue), 3)))
            
    def toradFunction(inputValue : float):
        print(inputValue, " degrees converted to radians is", rad((inputValue)), " radians ")
        exit_flow(str(inputValue) + " degrees converted to radians is " + str(rad((inputValue))) + " radians ")
    
    def todegFunction(inputValue : float):
        print(inputValue, " radians converted to degrees is", deg(inputValue / 3.14 * math.pi), " degrees ")
        exit_flow(str(inputValue) + " radians converted to degrees is " + str(deg(inputValue / 3.14 * math.pi)) + " degrees ")
        
    def promt():
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
    
    def decide(choice : str):
        if choice in ('1', '2', '3', '4', '5', '6'):
                numbers = safeInputDoubleValue("Value for the first number", "Value for the second number")
                match choice:
                    case '1':
                        addFunction(numbers)
                    
                    case '2':
                        subtFunction(numbers)
    
                    case '3':
                        multFunction(numbers)
    
                    case '4':
                        divFunction(numbers)
        
                    case '5':
                        sqrFuction(numbers)
                        
                    case '6':
                        modFunction(numbers)
                            
        else: 
            number = safeInputSingleValue("Enter Number")
            match choice:
                case '7':
                    sqrFuction(number)
            
                case '8':
                    circFunction(number)
            
                case '9':
                    ciraFunction(number)
            
                case '10':
                    sinFunction(number)
          
                case '11':
                    cosFunction(number)
            
                case '12':
                    tanFunction(number)
          
                case '13':
                    toradFunction(number)
         
                case '14':
                    todegFunction(number)
                
                case '15':
                    read_file()
                    exit_flow("15")        
                    
                case _: #  if operation choice is not within the range of 1-15, return error message to user and prompt them again
                    print("Invalid operation selected, please try again")
                    time.sleep(2)
    
    def legDecide(choice : str):
        if choice.__eq__("-E"):
            sys.exit(0)
            
        if choice in ('1', '2', '3', '4', '5', '6'):
            numbers = safeInputDoubleValue("Value for the first number", "Value for the second number")            
            if choice=='1':
                addFunction(numbers)
                    
            elif choice=='2':
                subtFunction(numbers)
    
            elif choice=='3':
                multFunction(numbers)
    
            elif choice=='4':
                divFunction(numbers)
        
            elif choice=='5':
                sqrFuction(numbers)
                        
            elif choice=='6':
                modFunction(numbers)
                            
        else: 
            number = safeInputSingleValue("Enter Number")
            if choice=='7':
                sqrtFunction(number)
            
            elif choice=='8':
                circFunction(number)
        
            elif choice=='9':
                ciraFunction(number)
        
            elif choice=='10':
                sinFunction(number)
            
            elif choice=='11':
                cosFunction(number)
        
            elif choice=='12':
                tanFunction(number)
            
            elif choice=='13':
                toradFunction(number)
            
            elif choice=='14':
                todegFunction(number)
                    
            elif choice=='15':
                read_file()
                exit_flow("15")        
                    
            else: #  if operation choice is not within the range of 1-15, return error message to user and prompt them again
                print("Invalid operation selected, please try again")
                time.sleep(2)
    
                
    def interact():
        #promt options
        promt()
        # Making the calculator work
        while True:
            # todo: fix spacing issues in output to file
            # For every choice, execute operations based on user input
            choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13/14/15): ")
            if versionCheck():
                decide(choice)
            else:
                legDecide(choice)
    
    #functionality of calculator starts here
    interact()

#extra fail save
try:
    calculator()
except BaseException as err:
    print("Exception:"+str(err))
# :)
