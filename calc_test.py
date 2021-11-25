from calc import *

if (add(1, 2) == 3 and add(2, 2) == 4):
    print("Add test passed")
else:
    print("Add test failed: " + str(add(1, 2)))

if (subtract(2, 1) == 1 and subtract(2, 2) == 0):
    print("Subtract test passed")
else:
    print("Subtract test failed: " + str(subtract(2, 1)))

if (multiply(2, 2) == 4 and multiply(2, 1) == 2):
    print("Multiply test passed")
else:
    print("Multiply test failed: " + str(multiply(2, 2)))




