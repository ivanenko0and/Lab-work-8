
"""
По найменуванню виробника виводить на екран дані про об'єкти комплектації із зазначенням кількості на складі.
"""

answer = '1'
while answer == '1':

    d = {"процесор": {}, "материнська плата": {}, "пам'ять": {},
         "відео карта": {}, "звукова карта": {}, "вінчестер": {}}
    # d - словник даних про об'єкти комплектації комп'ютера на складі

    # Введення даних про об'єкти комплектації комп'ютера:
    print(f"Вводьте назви виробників для об'єктів комплектації комп'ютера та їх кількість від цих виробників \
(натисніть пробіл для припинення вводу):")
    for i in d:
        print(f" ─ {i}:")
        n1 = n2 = 0
        while True:  # Для кожного об'єкти комплектації записується виробник та їх кількість від цього виробника
            while True:
                try:
                    n1 = input(f"Виробник {len(d[i]) + 1}:")
                    break
                except ValueError:
                    print("Вводьте правильні дані!")
            if n1 == " " or n1 == "":  # Введення продовжується поки не буде записаний пропуск
                break
            while True:
                try:
                    n2 = int(input("Кількість:"))
                    if n2 >= 0:
                        break
                    else:
                        print("Вводьте правильні дані!")
                except ValueError:
                    if n2 == int():
                        break
                    print("Вводьте правильні дані!")
            if n2 == int():
                break
            d[i][n1] = n2

    pr_d = {}  # словник даних про об'єкти комплектації комп'ютера на складі відносно їх виробників
    for i in d:  # заповнення pr_d на основі даних словника d:
        for j in d[i]:
            if j not in pr_d:
                pr_d[j] = {}
            pr_d[j][i] = d[i][j]

    answer2 = '2'
    while answer2 == '2':

        print("─────────────────────────────────────")
        while True:  # Введення назви виробника із вже записаних
            k = input("Введіть назву виробника:")
            if k in pr_d:
                break
            else:
                print("Введіть правильну назву!")

        print("─────────────────────────────────────")
        print("Перелік об'єктів комплектації комп'ютера з їх кількістю заданого виробника:")
        for i in pr_d[k]:  # Виведення даних про об'єкти комплектації комп'ютера від заданого виробника
            print(f"  {i} - {pr_d[k][i]}")

        # Повторення запиту на назву виробника при введенні користувачем двійки:
        answer2 = input("Введіть '2' для повторення:")

    answer = input("Введіть '1' для повторного введення даних:")

# Виконав Іваненко Андрій Вадимович
