#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Exp:
    """
    Класс для представления числа и его степени.
    first - дробное число (основание)
    second - целое число (показатель степени)
    """

    def __init__(self, first=0.0, second=0):
        self.first = float(first)
        self.second = int(second)

    # Свойства для доступа к приватным полям
    @property
    def first(self):
        return self.__first

    @first.setter
    def first(self, value):
        self.__first = float(value)

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, value):
        self.__second = int(value)

    # Перегрузка оператора ** для возведения в степень
    def __pow__(self, power):
        """Перегрузка оператора ** - возвращает результат возведения в степень"""
        if power is None:
            return self.power()
        return self.first ** power

    # Перегрузка оператора @ для вызова power()
    def __matmul__(self, other):
        """Перегрузка оператора @ для вызова метода power()"""
        return self.power()

    # Перегрузка оператора << для ввода данных
    def __lshift__(self, prompt):
        """Перегрузка оператора << для ввода данных"""
        if isinstance(prompt, str):
            self.read(prompt)
        return self

    # Перегрузка оператора >> для вывода данных
    def __rshift__(self, other):
        """Перегрузка оператора >> для вывода данных"""
        self.display()
        return self

    # Перегрузка оператора + для сложения результатов
    def __add__(self, other):
        """Сложение результатов возведения в степень"""
        if isinstance(other, Exp):
            return self.power() + other.power()
        return self.power() + other

    # Перегрузка оператора - для вычитания результатов
    def __sub__(self, other):
        """Вычитание результатов возведения в степень"""
        if isinstance(other, Exp):
            return self.power() - other.power()
        return self.power() - other

    # Перегрузка оператора * для умножения результатов
    def __mul__(self, other):
        """Умножение результатов возведения в степень"""
        if isinstance(other, Exp):
            return self.power() * other.power()
        return self.power() * other

    # Перегрузка оператора / для деления результатов
    def __truediv__(self, other):
        """Деление результатов возведения в степень"""
        if isinstance(other, Exp):
            return self.power() / other.power()
        return self.power() / other

    # Перегрузка оператора == для сравнения
    def __eq__(self, other):
        """Сравнение по результату возведения в степень"""
        if isinstance(other, Exp):
            return self.power() == other.power()
        return self.power() == other

    # Перегрузка оператора < для сравнения
    def __lt__(self, other):
        """Сравнение по результату возведения в степень"""
        if isinstance(other, Exp):
            return self.power() < other.power()
        return self.power() < other

    # Перегрузка оператора > для сравнения
    def __gt__(self, other):
        """Сравнение по результату возведения в степень"""
        if isinstance(other, Exp):
            return self.power() > other.power()
        return self.power() > other

    # Перегрузка оператора <= для сравнения
    def __le__(self, other):
        """Сравнение по результату возведения в степень"""
        if isinstance(other, Exp):
            return self.power() <= other.power()
        return self.power() <= other

    # Перегрузка оператора >= для сравнения
    def __ge__(self, other):
        """Сравнение по результату возведения в степень"""
        if isinstance(other, Exp):
            return self.power() >= other.power()
        return self.power() >= other

    # Перегрузка оператора bool() для проверки истинности
    def __bool__(self):
        """Проверка, не является ли результат нулем"""
        return self.power() != 0

    # Перегрузка оператора str() для строкового представления
    def __str__(self):
        return f"{self.first} ^ {self.second}"

    def __repr__(self):
        return f"Exp({self.first}, {self.second})"

    # Перегрузка оператора call для вызова power()
    def __call__(self):
        """Вызов объекта как функции возвращает результат power()"""
        return self.power()

    # Перегрузка оператора | для создания нового объекта
    def __or__(self, other):
        """Создание нового объекта с другим показателем степени"""
        if isinstance(other, (int, float)):
            return Exp(self.first, int(other))
        return Exp(self.first, other.second)

    # Перегрузка оператора & для создания нового объекта
    def __and__(self, other):
        """Создание нового объекта с другим основанием"""
        if isinstance(other, (int, float)):
            return Exp(float(other), self.second)
        return Exp(other.first, self.second)

    # Прочитать значение (оригинальный метод)
    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(float, line.split(' ^ ', maxsplit=1)))

        self.first = float(parts[0])
        self.second = int(parts[1])
        return self

    # Вывести на экран (оригинальный метод)
    def display(self):
        print(f"{self.first} ^ {self.second}")
        return self

    # Возведение в степень (оригинальный метод)
    def power(self):
        """Основной метод возведения в степень"""
        try:
            return self.first ** self.second
        except ZeroDivisionError:
            if self.first == 0 and self.second < 0:
                raise ValueError("Невозможно возвести 0 в отрицательную степень")
            raise
        except OverflowError:
            raise ValueError("Результат слишком большой")


def make_exp(first, second):
    """
    Функция создания экземпляра класса Exp, принимая значения полей как аргументы
    """
    return Exp(first, second)


if __name__ == '__main__':
    print("Демонстрация работы класса Exp с перегруженными операторами:")
    print("=" * 50)

    # 1. Использование операторов ввода/вывода >>
    print("\n1. Ввод/вывод с помощью операторов << и >>:")
    exm1 = Exp() << "Введите степень в формате 'число ^ степень': "
    exm1 >> None  # Вывод на экран

    # 2. Использование оператора @ для power()
    print("\n2. Использование оператора @ для вычисления:")
    result = exm1 @ None
    print(f"Результат: {result}")

    # 3. Использование оператора вызова ()
    print("\n3. Использование оператора вызова ():")
    print(f"Результат вызова: {exm1()}")

    # 4. Создание объектов с помощью операторов | и &
    print("\n4. Создание новых объектов с помощью | и &:")
    exm2 = exm1 | 5  # Новый объект с той же базой, но степенью 5
    exm3 = exm1 & 10.5  # Новый объект с той же степенью, но базой 10.5

    print(f"Исходный: {exm1}")
    print(f"exm1 | 5: {exm2}")
    print(f"exm1 & 10.5: {exm3}")

    # 5. Арифметические операции
    print("\n5. Арифметические операции:")
    exm4 = Exp(2, 3)  # 8
    exm5 = Exp(3, 2)  # 9

    print(f"{exm4} + {exm5} = {exm4 + exm5}")  # 17
    print(f"{exm4} - {exm5} = {exm4 - exm5}")  # -1
    print(f"{exm4} * {exm5} = {exm4 * exm5}")  # 72
    print(f"{exm4} / {exm5} = {exm4 / exm5:.2f}")  # 0.89

    # 6. Операции сравнения
    print("\n6. Операции сравнения:")
    print(f"{exm4} == {exm5}: {exm4 == exm5}")
    print(f"{exm4} < {exm5}: {exm4 < exm5}")
    print(f"{exm4} > {exm5}: {exm4 > exm5}")

    # 7. Проверка на истинность
    print("\n7. Проверка на истинность:")
    exm6 = Exp(0, 5)
    exm7 = Exp(2, 3)
    print(f"bool({exm6}): {bool(exm6)}")
    print(f"bool({exm7}): {bool(exm7)}")

    # 8. Использование функции make_exp
    print("\n8. Использование функции make_exp:")
    exm8 = make_exp(4.5, 2)
    exm8.display()
    print(f"Результат: {exm8.power()}")

    # 9. Обработка особых случаев
    print("\n9. Обработка особых случаев:")
    try:
        exm9 = Exp(0, -1)
        print(f"Результат: {exm9.power()}")
    except ValueError as e:
        print(f"Ошибка: {e}")