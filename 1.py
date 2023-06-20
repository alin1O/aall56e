#Евлоева Алина Борисовна Группа 44-22-115 Вариант 7 Задание 1
import math

def calculate_value(x):
    if x >= 0:
        return math.sqrt(x ** 3)
    else:
        return math.log(abs(x))
try:
    x = float(input("Введите значение x: "))
    result = calculate_value(x)
    print("Результат:", result)
except ValueError:
    print("Ошибка ввода числа")
except Exception as e:
    print("Ошибка:", e)