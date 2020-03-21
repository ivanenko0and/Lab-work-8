"""
Виконайте добуток двох квадратних матриць 3*3, врахуйте розмірність.
Результати множення елементів занесіть до нової матриці та виведіть її на екран.
"""

import numpy as np

answer = '1'
while answer == '1':

    # array3 - масив 3*3, елементи якого є добутками відповідних елментів масивів (3*3) array1 і array2
    array1, array2, array3 = np.zeros((3, 3), dtype=int), np.zeros((3, 3), dtype=int), np.zeros((3, 3), dtype=int)
    maxl = 0  # maxl - змінна для форматного виведення

    print("Введіть значення елементів першого масиву розмірності 3 на 3:")
    for i in range(3):  # Поелементне введення значення масиву array1:
        print(f"Введіть значення {i + 1} рядка:")
        for j in range(3):
            while True:
                try:
                    array1[i][j] = int(input())
                    break
                except ValueError:
                    print("Вводьте правильні дані!")
                except OverflowError:  # Зловлення помилки щодо занадто великого значення елементу масива
                    print("Вводьте правильні дані!")
    print("Введіть значення елементів другого масиву розмірності 3 на 3:")
    for i in range(3):  # Поелементне введення значення масиву array2:
        print(f"Введіть значення {i + 1} рядка:")
        for j in range(3):
            while True:
                try:
                    array2[i][j] = int(input())
                    break
                except ValueError:
                    print("Вводьте правильні дані!")
                except OverflowError:  # Зловлення помилки щодо занадто великого значення елементу масива
                    print("Вводьте правильні дані!")

    # Знаходження добутку масивів array1 і array2:
    for i in range(3):
        for j in range(3):
            for k in range(3):
                array3[i][j] += array1[i][k] * array2[k][j]
            if len(str(array3[i][j])) > maxl:  # Визначення maxl - максимальної довжини елемента масиву
                maxl = len(str(array3[i][j]))

    # Форматне виведення масиву array3 у вигляді таблиці:
    print("Добуток цих двох масивів дорівнює:")
    print(f"{'':─^{maxl * 3 + 10}}")
    for i in range(3):
        for j in range(3):
            print(f"| {array3[i][j]:^{maxl}} ", end="")
        print("|")
        print(f"{'':─^{maxl * 3 + 10}}")

    answer = input("Введіть '1' для повторення:")

# Виконав Іваненко Андрій Вадимович
