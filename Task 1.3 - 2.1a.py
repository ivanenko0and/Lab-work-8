
# Алгоритм лінійного пошуку


answer = '1'
while answer == '1':

    string, element = [], 0  # string - задана послідовність, element - шукане значення

    print("Введіть послідовність (натисніть пробіл для припинення вводу):")
    while True:  # Введення значень n, які будуть додаватись до послідовності string як елементи:
        n = input()
        if n == " " or n == "":  # Якщо значення n є пропуском, то введення завершується
            break
        else:  # В іншому випадку значення n додається до послідовності string
            for i in n:  # Якщо n є послідовністю, то всі її елементи окремо додаються
                string.append(i)
            continue

    print("Введіть шуканий елемент:")
    while True:  # Введення значення element:
        element = input()
        if len(element) > 1:  # Якщо значення element є послідовністю, то введення повторюється
            print("Введіть одиничне значення!")
        else:
            break

    index = checks = 0  # index - номер шуканого значення, checks - кількість перевірок
    string_length = len(string)  # string_length - довжина заданої послідовності
    # Поелементна перевірка послідовності string на наявність element:
    while index < string_length and element != string[index]:
        """ Якщо елемент string з номером index не дорівнює element, index збільшується на один доки не відбудеться збіг 
            або index не стане більше за довжину string"""
        index += 1
        checks += 1  # Також з кожною перевіркою збільшується значення checks
    checks += 1  # Додаємо одиницю до значення checks, оскільки остання перевірка у циклі не зараховується

    """ Якщо index менше за довжину string, то element знайдено
    При знаходженні element виводиться його порядковий номер у послідовності string та кількість перевірок: """
    if index < string_length:
        print(f"Елемент знайдено на позиції {index}.")
        print(f"Кількість виконаних порівнянь дорівнює {checks}.")
    else:  # Якщо index більше за довжину string, то element не знайдено
        print("Елемент не знайдено.")

    answer = input("Введіть '1' для повторення:")

# Виконав Іваненко Андрій Вадимович
