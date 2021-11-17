import math
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


def calculator():
    def safe_input_single_value(prompt_message: str) -> float:
        value = None
        while value == None:
            value = safe_convert(input(prompt_message), None, float)

        return value

    def safeInputDoubleValue(PromptMessage1: str, PromptMessage2: str) -> tuple:
        number_1 = None
        number_2 = None

        while number_1 is None or number_2 is None:
            print(
                "repeat if bad value is entered (bad values are anything that is not a number)"
            )
            number_1 = safe_convert(input(PromptMessage1), None, float)
            number_2 = safe_convert(input(PromptMessage2), None, float)

        return (number_1, number_2)

    def run_and_round2_value(number_1: float, number_2: float, func) -> float:
        return round(func(number_1, number_2), int(input("Rounding place: ")))

    def run_and_round1_value(number_1: float, func) -> float:
        return round(func(number_1), int(input("Rounding place: ")))

    def add(number_1: float, number_2: float) -> float:
        return number_1 + number_2

    # subtracting

    def subtract(number_1: float, number_2: float) -> float:
        return number_1 - number_2

    # multiplying

    def multiply(number_1: float, number_2: float) -> float:
        return number_1 * number_2

    # dividing

    def divide(number_1: float, number_2: float) -> float:
        return number_1 / number_2

    # exponentiation

    def exponent(number_1: float, number_2: float) -> float:
        return number_1 ** number_2

    # modulo/remainder/whatever you want to call it

    def modulo(number_1: float, number_2: float) -> float:
        return number_1 % number_2

    # square root

    def sqrroot(number_1: float) -> float:
        return exponent(number_1, 0.5)

    # circumference

    def circumference(number_1: float) -> float:
        return math.pi * number_1

    # area of circle

    def circle_area(number_1: float) -> float:
        return math.pi * (number_1 ** 2)

    # sin, cos, tan

    def sin(number_1: float) -> float:
        return math.sin(number_1)

    def cos(number_1: float) -> float:
        return math.cos(number_1)

    def tan(number_1: float) -> float:
        return math.tan(number_1)

    def rad(number_1: float) -> float:
        return math.radians(number_1)

    def deg(number_1: float) -> float:
        return math.degrees(number_1)

    def rad_or_degree() -> bool:  # rad or degree choice picker function
        vrad_or_degree = safe_input_single_value(
            "Degrees or radians? Enter 0 for degrees, 1 for radians: "
        )
        if vrad_or_degree == 1 or vrad_or_degree == 0:
            return True if vrad_or_degree == 1 else False
        else:
            print("Must select 1 or 0")
            time.sleep(2)

    def add_function(inputs: tuple):
        print(
            inputs[0],
            "+",
            inputs[1],
            "=",
            run_and_round2_value(inputs[0], inputs[1], add),
        )
        exit_flow(
            str(inputs[0]) + "+" + str(inputs[1]) + "=" + str(add(inputs[0], inputs[1]))
        )

    def subt_function(inputs: tuple):
        print(
            inputs[0],
            "-",
            inputs[1],
            "=",
            run_and_round2_value(inputs[0], inputs[1], subtract),
        )
        exit_flow(
            str(inputs[0])
            + "-"
            + str(inputs[1])
            + "="
            + str(subtract(inputs[0], inputs[1]))
        )

    def mult_function(inputs: tuple):
        print(
            inputs[0],
            "*",
            inputs[1],
            "=",
            run_and_round2_value(inputs[0], inputs[1], multiply),
        )
        exit_flow(
            str(inputs[0])
            + "*"
            + str(inputs[1])
            + "="
            + str(multiply(inputs[0], inputs[1]))
        )

    def div_function(inputs: tuple):
        if inputs[1] == 0:  # if user attempts to input by 0, return error message
            print("Oops! Numbers cannot be divided by 0")
        else:
            print(
                inputs[0],
                "/",
                inputs[1],
                "=",
                run_and_round2_value(inputs[0], inputs[1], divide),
            )
            exit_flow(
                str(inputs[0])
                + "/"
                + str(inputs[1])
                + "="
                + str(divide(inputs[0], inputs[1]))
            )

    def sqr_function(inputs: tuple):
        print(
            inputs[0],
            "to the power of",
            inputs[1],
            "=",
            run_and_round2_value(inputs[0], inputs[1], exponent),
        )
        exit_flow(
            str(inputs[0])
            + "to the power of"
            + str(inputs[1])
            + "="
            + str(exponent(inputs[0], inputs[1]))
        )

    def mod_function(inputs: tuple):
        if inputs[1] == 0:  # if user attempts to input by 0, return error message
            print("Oops! Numbers cannot be divided by 0")
        else:
            print(
                inputs[0],
                "/",
                inputs[1],
                "=",
                run_and_round2_value(inputs[0], inputs[1], modulo),
            )
            exit_flow(
                str(inputs[0])
                + "/"
                + str(inputs[1])
                + "="
                + str(modulo(inputs[0], inputs[1]))
            )

    def sqrt_function(input_value: float):
        print(
            "The square root of",
            input_value,
            "is",
            run_and_round1_value(input_value, sqrroot),
        )
        exit_flow(
            "The square root of" + str(input_value) + "is" + str(sqrroot(input_value))
        )

    def circumference_function(input_value: float):
        print(
            "A circle with diameter",
            input_value,
            "has a circumference of",
            run_and_round1_value(input_value, circumference),
        )
        exit_flow(
            "A circle with diameter"
            + str(input_value)
            + "has a circumference of"
            + str(circumference(input_value))
        )

    def area_function(input_value: float):
        print(
            "A circle with radius",
            input_value,
            "has an area of",
            run_and_round1_value(input_value, circle_area),
        )
        exit_flow(
            "A circle with radius"
            + str(input_value)
            + "has an area of"
            + str(circle_area(input_value))
        )

    def sin_function(input_value: float):
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

    def cos_function(input_value: float):
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

    def tan_function(input_value: float):
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

    def to_rad_function(input_value: float):
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

    def dic_function_runner_with_0_input(func):
        func()

    def dic_function_runner_with_2_input(args: tuple, func):
        func(args)

    def dic_function_runner_with_1_input(arge: float, func):
        func(arge)

    def new_interact():
        while True:
            prompt()
            choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13/14/15):")
            if choice.__eq__("-E"):
                sys.exit(0)

            if choice in ("1", "2", "3", "4", "5", "6"):
                numbers = safeInputDoubleValue(
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

    # functionality of calculator starts here
    new_interact()


# extra fail save
try:
    calculator()

except SystemExit:
    pass

except BaseException as err:
    print("Exception:" + str(err))
# :)
