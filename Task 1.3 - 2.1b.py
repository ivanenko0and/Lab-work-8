
# Алгоритм лінійного пошуку


def linear_search(s, x):  # s - задана послідовність, x - шукане значення

    # Виведення значення послідовності s поелементно та значення шуканого елемента x:
    print("Задана послідовність: ", end="")
    for i in range(len(s)):
        if i == len(s) - 1:
            print(s[i])
        else:
            print(s[i], end=", ")
    print(f"Шуканий елемент: {x}")

    index = checks = 0  # index - номер шуканого значення, checks - кількість перевірок
    s_length = len(s)  # string_length - довжина заданої послідовності
    # Поелементна перевірка послідовності s на наявність x:
    while index < s_length and x != s[index]:
        index += 1
        checks += 2  # Також з кожною перевіркою збільшується значення checks
    checks += 2  # Збільшуємо значення checks, оскільки остання перевірка у циклі не зараховується

    # Якщо index менше за довжину s, то x знайдено
    # При знаходженні element виводиться його порядковий номер у послідовності s та кількість перевірок:
    if index < s_length:
        print(f"Елемент знайдено на позиції {index}.")
        print(f"Кількість виконаних порівнянь дорівнює {checks}.")
    else:  # Якщо index більше за довжину s, то element не знайдено
        print("Елемент не знайдено.")


linear_search('Linear search algorithm', 'c')
"""
Елемент знайдено на позиції 11.
Кількість виконаних порівнянь дорівнює 24.
"""

print("───────────────────────────────")
linear_search([5, 7, 2, 7, 4, 6, 3, 5], 3)
"""
Елемент знайдено на позиції 6.
Кількість виконаних порівнянь дорівнює 14.
"""

print("───────────────────────────────")
linear_search(range(10, 30), 38)
"""
Елемент не знайдено.
"""

# Виконав Іваненко Андрій Вадимович
