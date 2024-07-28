import requests
import json
import sqlite3 as sl
import csv
from datetime import datetime as dt


# 1. Подключение к API и получение данных
# Напишите скрипт на Python, который подключается к API и получает данные. Например, используйте публичное API
# https://jsonplaceholder.typicode.com/posts. Сохраните полученные данные в формате JSON в файл.

my_url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url=my_url)
with open('my_json.json', 'w') as f:
    json.dump(response.json(), f)


# 2. Обработка данных с использованием SQL
# Представьте, что у вас есть таблица users в базе данных SQLite с полями id, name, и age. Напишите Python-скрипт,
# который подключается к этой базе данных, выбирает всех пользователей старше 30 лет и выводит их имена и возраст.

conn = sl.connect('sqlite_db')
cur = conn.cursor()
result_obj = cur.execute('select name, age from zarma_users where age > 30')
for user in result_obj:
    print(f'Пользователь: {user[0]}; Возраст: {user[1]}')


# 3. Объединение данных из разных источников
# Напишите скрипт на Python, который объединяет данные из двух источников. Первый источник - это CSV-файл с
# информацией о продуктах (поля: product_id, product_name). Второй источник - это JSON-файл с данными
# о продажах (поля: sale_id, product_id, amount). Скрипт должен объединить данные по product_id
# и вывести итоговую таблицу с информацией о продажах для каждого продукта.

product_file = open('product.csv')
product_obj = csv.reader(product_file)

sales_file = open('sales.json')
sales_list = json.load(sales_file)

product_sales = {}

for i, product in enumerate(product_obj):
    if i != 0:
        sale_amount = 0
        for sale in sales_list:
            if sale['product_id'] == int(product[0]):
                sale_amount += sale['amount']
        product_sales[product[1]] = sale_amount

product_file.close()
sales_file.close()

print(product_sales)


# 4. Оптимизация скрипта
# Дан следующий скрипт на Python для обработки списка чисел. Оптимизируйте его для повышения производительности.
# Исходный скрипт

start_time = dt.now()
numbers = [i for i in range(1, 1000001)]
squares = []
for number in numbers:
    squares.append(number ** 2)
finish_time = dt.now()
processing_time_1 = finish_time - start_time
print(f'Исходное время выполнения в микросекундах: {processing_time_1.microseconds}')

# Оптимизированный скрипт

def my_generator(my_list):
    my_index = 0
    yield my_list[my_index]
    my_index += 1


start_time = dt.now()
squares = []
for number in my_generator(numbers):
    squares.append(number ** 2)
finish_time = dt.now()
processing_time_2 = finish_time - start_time
print(f'Оптимизированное время выполнения в микросекундах: {processing_time_2.microseconds}')
print(f'Производительность повысилась в {round(processing_time_1.microseconds/processing_time_2.microseconds)} раз(-а)')
