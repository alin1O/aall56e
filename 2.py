#Евлоева Алина Борисовна Группа 44-22-115 Вариант 7 Задание 2
import unittest

class CalculationTest(unittest.TestCase):
    def test_case_x_greater_than_or_equal_to_0(self):
        result = calculate_value(4)
        self.assertEqual(result, math.sqrt(4 ** 3))

    def test_case_x_less_than_0(self):
        result = calculate_value(-2)
        self.assertEqual(result, math.log(abs(-2)))

if __name__ == '__main__':
    unittest.main()