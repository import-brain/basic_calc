def add(x,y):
    return x + y


def subtract(x,y):
    return x - y


def multiply(x,y):
    return x * y


def divide(x,y):
    return x / y

print("Select operation")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

while True:

    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
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
        break
    else:
        print("Invalid input: select operation")

input("Thank you for using my calculator! Press enter to exit")
