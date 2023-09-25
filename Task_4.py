# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

def calculate_fraction_operations(fraction1, fraction2):
    fraction1 = Fraction(fraction1)
    fraction2 = Fraction(fraction2)

    sum_result = fraction1 + fraction2
    product_result = fraction1 * fraction2

    return sum_result, product_result


fraction1 = input("Введите первую дробь (в формате a/b): ")
fraction2 = input("Введите вторую дробь (в формате a/b): ")

sum_result, product_result = calculate_fraction_operations(fraction1, fraction2)

print("Сумма дробей:", sum_result)
print("Произведение дробей:", product_result)
