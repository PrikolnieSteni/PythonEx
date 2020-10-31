import random
import math


def IsSimple(number):
    d = 2
    while number % d != 0:
        d += 1
    return d == number


def Point1(numbers):
    def a():
        min_number = min([i for i in numbers if i % 2 == 0])
        print('Минимальное четное число: ', min_number)
        return min_number

    def b():
        simple_number = [i for i in numbers if IsSimple(i) == True]
        print('Минимальное простое число: ', min(simple_number))
        return min(simple_number)

    def c():
        average_number = sum(numbers) / len(numbers)
        dict_deltas = {}
        for i, k in enumerate(numbers):
            dict_deltas[abs(k - average_number)] = k
        print('Число, ближе всего по значению к среднему: ', dict_deltas.get(min(dict_deltas.keys())))
        return dict_deltas.get(min(dict_deltas.keys()))

    def d():
        sqr_numbers = {}
        for i, k in enumerate(numbers):
            sqr_numbers[k ** 2] = k
        print(sqr_numbers)
        print(min(sqr_numbers.keys()))
        return sqr_numbers.get(min(sqr_numbers.keys()))

    functions = ['a', 'b', 'c', 'd']

    while True:
        option = input('Выберите пункт меню: ')
        if option in functions:
            if option == 'a':
                obj = a()
            if option == 'b':
                obj = b()
            if option == 'c':
                obj = c()
            if option == 'd':
                obj = d()
            break
        else:
            continue
    return numbers.index(obj)


def Point2(index, numbers):
    def a():
        try:
            residue_numbers = [i for i in numbers if i // index == 0]
            if not residue_numbers:
                return print('Значений нет!')
            else:
                return print('Элементы, которые делятся на найденное значение без остатка', residue_numbers)
        except ZeroDivisionError:
            print('Деление на ноль!')

    def b():
        next_numbers = numbers[index + 1:index + 6]
        if not next_numbers:
            return print('Значений нет!')
        else:
            return print('Элементы, находящиеся правее индекса значения', next_numbers)

    def c():
        even_numbers = [i for i in numbers if numbers.index(i) % 2 == 0 and i < numbers[index]]
        if not even_numbers:
            return print('Значений нет!')

        else:
            return print('Значения, находящиеся в четных по индексу элементах и меньше найденного значения', even_numbers)


    def d():
        value = numbers[index]
        numbers.remove(numbers[index])
        sqrt_numbers = [i for i in numbers if i >= 0 and math.sqrt(i) < value]
        if not sqrt_numbers:
            return print('Значений нет!')
        else:
            return print('Значения, корень которых меньше найденного значения ', sqrt_numbers)


    functions = ['a', 'b', 'c', 'd']

    while True:
        option = input('Выберите пункт меню: ')
        if option in functions:
            if option == 'a':
                obj = a()
            if option == 'b':
                obj = b()
            if option == 'c':
                obj = c()
            if option == 'd':
                obj = d()
            break
        else:
            continue

while True:
    try:
        numbers_count = int(input('Введите количество: '))
        break
    except Exception as e:
        print('Ошибка')
print('Задание 1:')
numbers = [random.randint(-100, 100) for i in range(numbers_count)]
print('Исходный ряд: ', numbers)
number = Point1(numbers)
print('Задание 2:')
print('Индекс элемента: ', number)
print('Задание 3:')
Point2(number, numbers)