# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


def decimal_to_hexadecimal(num):
    hexadecimal = hex(num)[2:]
    return hexadecimal

number = int(input("Введите целое число: "))

hexadecimal_result = decimal_to_hexadecimal(number)
print("Шестнадцатеричное представление:", hexadecimal_result)

hexadecimal_check = hex(number)[2:]
print(
    "Проверка шестнадцатеричного представления с помощью функции hex():",
    hexadecimal_check,
)
