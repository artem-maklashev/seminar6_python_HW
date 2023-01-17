# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def GetNumber(message):
    isCorrect = False
    while isCorrect == False:
        try:
            number = float(input(message))
            isCorrect = True
        except ValueError:
            print("Введено не число. Повторите ввод ")
    return number


# def GetSum(numb):
#     sum = 0
#     number = str(numb)
#     for item in (number):
#         if item.isdigit():
#             sum += int(item)
#     return sum


number = GetNumber("Введите число ")
# print(f'{number} -> {GetSum(number)}')

get_sum2 = sum([int(x) for x in str(number) if x.isdigit()])
print(f'{number} -> {get_sum2}')
