import calc

class Test_Calc_Div_function:
    def test_div_function_1(self):
        result = calc.div_function([0, 0], ["1", "0.1"])

    def test_div_function_2(self):
        result = calc.div_function([0, 1.0], ["1", "0.1"])

    def test_div_function_3(self):
        result = calc.div_function([0, 0], ["1", "12.0"])

    def test_div_function_4(self):
        result = calc.div_function([0, 0], ["10", "3.14"])

    def test_div_function_5(self):
        result = calc.div_function([0, -1.0], ["0.1", "3.14"])

    def test_div_function_6(self):
        result = calc.div_function([], [])

