import math
import cmath # might be needed for imaginary numbers
import sys
import time
from platform import system

# all helper functions
def version_check() -> bool:
    """return true if it can use match case else false"""
    minimum_python_version = (3, 10)
    current_version = (sys.version_info.major, sys.version_info.minor)
    if current_version >= minimum_python_version:
        return True
    else:
        return False


def safe_convert(value: str, default_value: str, function):
    """conversion tool that can handle conversions, however, option for default valve is added incase conversion is failed"""
    try:
        return function(value)
    except ValueError:
        return default_value


# DO NOT port exit_flow!
def exit_flow(printed_message: str):

    if (
        printed_message != "15"
    ):  # if user chooses to read calculations from storage, don't prompt user to save calculation
        save_choice = input(
            "Do you wish to save your calculation to local storage? (Y for yes, N for no) "
        )

        if save_choice in ("number_2", "number_2", "yes", "Yes"):
            write_file(printed_message)
            time.sleep(1)
        elif save_choice in ("n", "N", "no", "No"):
            pass

    exit_choice = input(
        "Exit? Or perform another calculation? (Y for another calculation, N for exit) "
    )

    if exit_choice in ("number_2", "number_2", "yes", "Yes"):
        calculator()
    elif exit_choice in ("N", "n", "No", "no"):
        sys.exit(0)
    else:
        print("Invalid answer, please try again")
        time.sleep(2)
        exit_flow("number_1")


def write_file(what_to_write: str):
    file_name = str(input("Desired file name: (-E to cancel)") + ".txt")
    if file_name.__eq__("-E"):
        return

    try:  # try to create file, if file already exists (IOError), go into append mode, and if no error, also go into append mode
        save_file = open(file_name, "number_1")  # @UnusedVariable
    except IOError:
        with open(file_name, mode="a") as file_object:
            print(what_to_write, file=file_object)
    else:
        with open(file_name, mode="a") as file_object:
            print(what_to_write, file=file_object)
    print("Calculation saved to ", file_name)


def read_file():
    file_name = str(input("Which storage file would you like to read?(-E to exit)"))
    if file_name == "-E":
        return
    else:
        file_name += ".txt"
    try:
        with open(file_name, mode="r") as file_object:
            # todo: implement ability for user to pick how many previous calculations to print, error handling for if user picks more lines than the file contains
            for line in file_object:
                print(line, end="")
    # if file not found, return error
    except FileNotFoundError:
        print("File not found, please try again")
        time.sleep(1)
        read_file()

    pass

def safe_input_single_value(prompt_message: str) -> float:
    """Input utility that gets a float value as an output, it is protected using safe_convert"""
    value = None
    while value == None:
        value = safe_convert(input(prompt_message), None, float)
    return value

def safe_input_double_value(prompt_message_1: str, prompt_message_2: str) -> tuple:
    """Input utility that gets 2 float values and return them as a tuple, it is protected by safe_convert"""
    number_1 = None
    number_2 = None

    while number_1 is None or number_2 is None:
        print(
            "repeat if bad value is entered (bad values are anything that is not a number)"
        )
        number_1 = safe_convert(input(prompt_message_1), None, float)
        number_2 = safe_convert(input(prompt_message_2), None, float)

    return (number_1, number_2)

def run_and_round2_value(number_1: float, number_2: float, func, suppress_rounding: bool=False) -> float:
    """function that executes a function and auto rounds, acquires rounding place by asking for it, this function only support functions that use 2 arguments"""
    if suppress_rounding:
        return func(number_1, number_2)
    else:
        return round(func(number_1, number_2), safe_input_single_value("Rounding Place:"))

def run_and_round1_value(number_1: float, func, suppress_rounding: bool=False) -> float:
    """function that executes a function and auto rounds, acquires rounding place by asking for it, this function only support functions that use 1 arguments"""
    if suppress_rounding:
        return func(number_1)
    else:
        return round(func(number_1), safe_input_single_value("Rounding Place:"))

def add(number_1: float, number_2: float) -> float:
    """addition utility"""
    return number_1 + number_2

def subtract(number_1: float, number_2: float) -> float:
    """subtraction utility"""
    return number_1 - number_2

def multiply(number_1: float, number_2: float) -> float:
    """multiplication utility"""
    return number_1 * number_2

def divide(number_1: float, number_2: float) -> float:
    """division utility, Caution: *no built-in safety protection,
    please take this into consideration when using this function*"""
    return number_1 / number_2

def exponent(number_1: float, number_2: float) -> float:
    """exponent utility"""
    return number_1 ** number_2

def modulo(number_1: float, number_2: float) -> float:
    """modulo/remainder utility, Caution:*no built-in safety protection,
    please put this into consideration when using this function*"""
    return number_1 % number_2

def sqrroot(number_1: float) -> float:
    """square root utility"""
    return exponent(number_1, 0.5)

def circumference(number_1: float) -> float:
    """circle circumference utility"""
    return math.pi * number_1

def circle_area(number_1: float) -> float:
    """circle area utility"""
    return math.pi * (number_1 ** 2)

def sin(number_1: float) -> float:
    """sin utility"""
    return math.sin(number_1)

def cos(number_1: float) -> float:
    """cos utility, Caution:*no built-in safety protection,
    please put this into consideration when using this function*"""
    return math.cos(number_1)

def tan(number_1: float) -> float:
    """tan utility, Caution:*no built-in safety protection,
    please put this into consideration when using this function*"""
    return math.tan(number_1)

def rad(number_1: float) -> float:
    """to radian utility"""
    return math.radians(number_1)

def deg(number_1: float) -> float:
    """to degree utility"""
    return math.degrees(number_1)

def rad_or_degree() -> bool:
    """rad or degree choice picker function"""
    vrad_or_degree = safe_input_single_value(
        "Degrees or radians? Enter 0 for degrees, 1 for radians: "
    )
    if vrad_or_degree == 1 or vrad_or_degree == 0:
        return True if vrad_or_degree == 1 else False
    else:
        print("Must select 1 or 0")
        time.sleep(2)

def add_function(inputs: tuple, suppress_rounding: bool=False):
    """addition functionality wrapper, this is not a helper function"""
    print(
        inputs[0],
        "+",
        inputs[1],
        "=",
        run_and_round2_value(inputs[0], inputs[1], add, suppress_rounding),
    )
    if not suppress_rounding:
        exit_flow(
            str(inputs[0]) + "+" + str(inputs[1]) + "=" + str(add(inputs[0], inputs[1]))
        )

def subt_function(inputs: tuple, suppress_rounding: bool=False):
    """subtation functionality wrapper, this is not a helper function"""
    print(
        inputs[0],
        "-",
        inputs[1],
        "=",
        run_and_round2_value(inputs[0], inputs[1], subtract, suppress_rounding),
    )
    if not suppress_rounding:
        exit_flow(
            str(inputs[0])
            + "-"
            + str(inputs[1])
            + "="
            + str(subtract(inputs[0], inputs[1]))
        )

def mult_function(inputs: tuple, suppress_rounding: bool=False):
    """multiplication functionality wrapper, this is not a helper function"""
    print(
        inputs[0],
        "*",
        inputs[1],
        "=",
        run_and_round2_value(inputs[0], inputs[1], multiply, suppress_rounding),
    )
    if not suppress_rounding:
        exit_flow(
            str(inputs[0])
            + "*"
            + str(inputs[1])
            + "="
            + str(multiply(inputs[0], inputs[1]))
        )

def div_function(inputs: tuple, suppress_rounding: bool=False):
    """division functionality wrapper, this is not a helper function, divide by 0 check is implemented"""
    if inputs[1] == 0:  # if user attempts to input by 0, return error message
        print("Oops! Numbers cannot be divided by 0")
    else:
        print(
            inputs[0],
            "/",
            inputs[1],
            "=",
            run_and_round2_value(inputs[0], inputs[1], divide, suppress_rounding),
        )
        if not suppress_rounding:
            exit_flow(
                str(inputs[0])
                + "/"
                + str(inputs[1])
                + "="
                + str(divide(inputs[0], inputs[1]))
            )

def sqr_function(inputs: tuple, suppress_rounding: bool=False):
    """square functionality wrapper, this is not a helper function"""
    print(
        inputs[0],
        "to the power of",
        inputs[1],
        "=",
        run_and_round2_value(inputs[0], inputs[1], exponent, suppress_rounding),
    )
    if not suppress_rounding:
        exit_flow(
            str(inputs[0])
            + "to the power of"
            + str(inputs[1])
            + "="
            + str(exponent(inputs[0], inputs[1]))
        )

def mod_function(inputs: tuple, suppress_rounding: bool=False):
    """modulo functionality wrapper, this is not a helper function, divide by 0 check is implemented"""
    if inputs[1] == 0:  # if user attempts to input by 0, return error message
        print("Oops! Numbers cannot be divided by 0")
    else:
        print(
            inputs[0],
            "/",
            inputs[1],
            "=",
            run_and_round2_value(inputs[0], inputs[1], modulo, suppress_rounding)
        )
        if not suppress_rounding:
            exit_flow(
                str(inputs[0])
                + "/"
                + str(inputs[1])
                + "="
                + str(modulo(inputs[0], inputs[1]))
            )

def sqrt_function(input_value: float, suppress_rounding: bool=False):
    """square root functionality wrapper, this is not a helper function, imaginary number handling is not yet implemented"""
    print(
        "The square root of",
        input_value,
        "is",
        run_and_round1_value(input_value, sqrroot, suppress_rounding),
    )
    if not suppress_rounding:
        exit_flow(
            "The square root of" + str(input_value) + "is" + str(sqrroot(input_value))
        )

def circumference_function(input_value: float, suppress_rounding: bool=False):
    """circle circumference functionality wrapper, this is not a helper function"""
    print(
        "A circle with diameter",
        input_value,
        "has a circumference of",
        run_and_round1_value(input_value, circumference, suppress_rounding),
    )
    if not suppress_rounding:
        exit_flow(
            "A circle with diameter"
            + str(input_value)
            + "has a circumference of"
            + str(circumference(input_value))
        )

def area_function(input_value: float, suppress_rounding: bool=False):
    print(
        "A circle with radius",
        input_value,
        "has an area of",
        run_and_round1_value(input_value, circle_area, suppress_rounding),
    )
    if not suppress_rounding:
        exit_flow(
            "A circle with radius"
            + str(input_value)
            + "has an area of"
            + str(circle_area(input_value))
        )

def sin_function(input_value: float, suppress_rounding: bool=False):
    if rad_or_degree():
        print(
            "The sine of ",
            input_value,
            " degrees is ",
            run_and_round1_value(math.radians(input_value), sin),
        )
        exit_flow(
            "The sine of "
            + str(input_value)
            + " degrees is "
            + str(round(sin(math.radians(input_value)), 3))
        )
    else:
        print(
            "The sine of ",
            input_value,
            " radians is ",
            run_and_round1_value(input_value, sin),
        )
        exit_flow(
            "The sine of "
            + str(input_value)
            + " radians is "
            + str(round(sin(input_value), 3))
        )

def cos_function(input_value: float, suppress_rounding: bool=False):
    if rad_or_degree():
        print(
            "The cosine of ",
            input_value,
            " degrees is ",
            round(cos(math.radians(input_value)), 3),
        )
        exit_flow(
            "The cosine of "
            + str(input_value)
            + " degrees is "
            + str(round(cos(math.radians(input_value)), 3))
        )
    else:
        print(
            "The cosine of ",
            input_value,
            " radians is ",
            round(cos(input_value), 3),
        )
        exit_flow(
            "The cosine of "
            + str(input_value)
            + " radians is "
            + str(round(cos(input_value), 3))
        )

def tan_function(input_value: float, suppress_rounding: bool=False):
    type_choice = rad_or_degree()
    if cos(math.radians(input_value) if not (type_choice) else input_value) == 0:
        print(
            "Tangent of ",
            input_value,
            "degrees" if type_choice == 0 else "radians",
            "is undefined",
        )
        exit_flow(
            "Tangent of "
            + str(input_value)
            + ("degrees" if type_choice == 0 else "radians")
            + " is undefined"
        )

    if type_choice:
        print(
            "The tangent of ",
            input_value,
            " degrees is ",
            round(tan(math.radians(input_value)), 3),
        )
        exit_flow(
            "The tangent of "
            + str(input_value)
            + " degrees is "
            + str(round(tan(math.radians(input_value)), 3))
        )
    else:
        print(
            "The tangent of ",
            input_value,
            " radians is ",
            round(tan(input_value), 3),
        )
        exit_flow(
            "The tangent of "
            + str(input_value)
            + " radians is "
            + str(round(tan(input_value), 3))
        )

def to_rad_function(input_value: float, suppress_rounding: bool=False):
    print(
        input_value,
        " degrees converted to radians is",
        rad((input_value)),
        " radians ",
    )
    exit_flow(
        str(input_value)
        + " degrees converted to radians is "
        + str(rad((input_value)))
        + " radians "
    )

def to_deg_function(input_value: float):
    print(
        input_value,
        " radians converted to degrees is",
        deg(input_value / 3.14 * math.pi),
        " degrees ",
    )
    exit_flow(
        str(input_value)
        + " radians converted to degrees is "
        + str(deg(input_value / 3.14 * math.pi))
        + " degrees "
    )

def read_file_function():
    read_file()
    exit_flow("15")

if __name__ == "__main__":
    def calculator(switch_mode: bool, switcher: str=None, values: tuple=None):

        def prompt():
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

        double_inputs_dic = {
            "1": add_function,
            "2": subt_function,
            "3": mult_function,
            "4": div_function,
            "5": sqr_function,
            "6": mod_function,
        }
        single_inputs_dic = {
            "7": sqrt_function,
            "8": circumference_function,
            "9": area_function,
            "10": sin_function,
            "11": cos_function,
            "12": tan_function,
            "13": to_rad_function,
            "14": to_deg_function,
        }
        no_inputs_dic = {"15": read_file_function}

        def dic_function_runner_with_0_input(func, suppress_rounding: bool=False):
            func()

        def dic_function_runner_with_2_input(args: tuple, func, suppress_rounding: bool=False):
            func(args, suppress_rounding)

        def dic_function_runner_with_1_input(arge: float, func, suppress_rounding: bool=False):
            func(arge, suppress_rounding)

        def new_interact():
            while True:
                prompt()
                choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13/14/15):")
                if choice.__eq__("-E"):
                    sys.exit(0)

                if choice in ("1", "2", "3", "4", "5", "6"):
                    numbers = safe_input_double_value(
                        "Value for the first number: ", "Value for the second number: "
                    )
                    dic_function_runner_with_1_input(numbers, double_inputs_dic[choice])
                elif choice in ("7", "8", "9", "10", "11", "12", "13", "14"):
                    number = safe_input_single_value("Enter Number: ")
                    dic_function_runner_with_1_input(number, single_inputs_dic[choice])

                elif choice in ("15"):
                    dic_function_runner_with_0_input(no_inputs_dic[choice])

                else:
                    print("Invalid operation selected, please try again")
                    time.sleep(2)

        def switch_interact(switch: str):
            if switch in ("1", "2", "3", "4", "5", "6"):
                dic_function_runner_with_1_input(values, double_inputs_dic[switch], True)
            elif switch in ("7", "8", "9"): #10, 11, 12, 13, 14 temporarily disabled
                dic_function_runner_with_1_input(values[0], single_inputs_dic[switch], True)
            elif switch in ("15"):
                dic_function_runner_with_0_input(no_inputs_dic[switch], True)

            else:
                print("Invalid operation")

        # functionality of calculator starts here
        if not switch_mode:
            new_interact()
        else:
            switch_interact(switcher)


    # extra fail save
    try:
        if len(sys.argv) == 1:
            calculator(False)
        elif sys.argv[1] == "headless":
            value = None
            if len(sys.argv) == 4:
                value = (float(sys.argv[3]), None)
            elif len(sys.argv) >= 5:
                value = (float(sys.argv[3]), float(sys.argv[4]))
        
            calculator(True, sys.argv[2], value)
    except SystemExit:
        pass

    except BaseException as err:
        print("Exception:" + str(err))