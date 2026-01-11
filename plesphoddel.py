import re
import csv

# Task1: Все слова, после которых стоит запятая; всю информацию в квадратных скобках.
def Task1():
    with open('task1-ru.txt', 'r', encoding = 'utf-8') as f:
        text = f.read()
        mask = r"\b[А-Яа-яЁё]+\b(?=,)|\[[^\]]*]"
        # \b[А-Яа-яЁё]+\b(?=,) первая часть 
        # \b начало слова, [А-Яа-яЁё] любая буква, + сколько угодно раз, \b конец слова, (?=,) проверяет, что сразу после слова идёт запятая, но запятую не включает в результат
        # | или
        # \[[^\]]*] вторая часть
        # \[ так как спецсимвол выделяем слешом и результат [ 
        # [...] один символ из набора
        # ^ не, \] так как спецсимвол выделяем слешом и результат ]
        # [^\]] любой символ кроме ], * сколько угодно раз, ] просто ]
        results = re.findall(mask, text)
        print(*results, sep = ", ")

# Task2: Все обозначения цветов. 
def Task2():
    with open("task2.html", "r", encoding="utf-8") as f:
        text = f.read()
        mask = r'#[0-9a-fA-F]{3,8}' # регулярное выражение для HEX-цветов
        results = re.findall(mask, text)
        new_results = list(set(results))
        print(*new_results, sep=", ")

# Task3
def Task3():
    with open("task3.txt", "r") as f:
        text = f.read()
        id = re.findall(r'(?<!-)\b\d{1,4}\b(?!-)', text)
        surname = re.findall(r'[A-Z][a-z]+', text)
        email = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text)
        date = re.findall(r'\d\d\d\d-\d\d-\d\d', text)
        website = re.findall(r'\w+://.+?/', text)
    data = []
    for i in range(len(id)):
        data.append([id[i], surname[i], email[i], date[i], website[i]])
    with open('result3.csv', 'w', encoding='utf-8') as file:
        for row in data:
            file.write(", ".join(row) + "\n")

# Task_add
def Task_Add():
    with open("task_add.txt", "r") as f:
        text = f.read()
    date = re.findall(r'\d{1,4}[-/.]\d{1,4}[-/.]\d{1,4}', text)
    email = re.findall(r'(?<=\s)[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text)
    website = re.findall(r'(?<=\s)https?://\S+', text)
    print(*date, sep =', ', end ='\n')
    print(*email, sep =', ', end ='\n')
    print(*website, sep =', ', end ='\n')

Task1()
Task2()
Task3()
Task_Add()