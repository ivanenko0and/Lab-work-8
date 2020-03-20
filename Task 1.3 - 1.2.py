
"""
Виведіть на екран транспоновану матрицю 3*3 (початкова матриця задана користувачем).
"""

import numpy as np

answer = '1'
while answer == '1':

    array, maxl = np.zeros((3, 3), dtype=int), 0  # array - масив для транспонування
    # maxl - змінна для форматного виведення
    print("Введіть значення елементів масиву розмірності 3 на 3:")
    for i in range(3):  # Поелементне введення значення масиву array:
        print(f"Введіть значення {i + 1} рядка:")
        for j in range(3):
            while True:
                try:
                    array[i][j] = int(input())
                    if len(str(array[i][j])) > maxl:  # Визначення maxl - максимальної довжини елемента масиву
                        maxl = len(str(array[i][j]))
                    break
                except ValueError:
                    print("Вводьте правильні дані!")
                except OverflowError:  # Зловлення помилки щодо занадто великого значення елементу масива
                    print("Вводьте правильні дані!")

    transpose_array = np.zeros((3, 3), dtype=int)  # transpose_array - транспонований масив array
    for i in range(3):  # Заповнення масиву transpose_array:
        for j in range(3):
            transpose_array[j][i] = array[i][j]

    # Форматне виведення масиву transpose_array у вигляді таблиці:
    print("Транспонований масив від заданого дорівнює:")
    print(f"{'─':─^{maxl * 3 + 10}}")
    for i in range(3):
        for j in range(3):
            print(f"| {transpose_array[i][j]:^{maxl}} ", end="")
        print("|")
        print(f"{'─':─^{maxl * 3 + 10}}")

    answer = input("Введіть '1' для повторення:")

# Виконав Іваненко Андрій Вадимович
