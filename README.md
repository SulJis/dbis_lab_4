# Лабораторна робота №1. Варіант 14.
##Сліпченко Максим, КМ-81.
## Опис репозиторію:

### Директорія до запуску програми
```
dbis_lab1
├── main.py
├── data - треба створити
│   ├── Odata2019File.csv - треба додати
│   └── Odata2020File.csv - треба додати
├── scripts
│   ├── batches_to_sqltable.py
│   ├── csv_to_batches.py
│   └── small_funcs.py
└── sql_queries
    ├── CREATE.sql
    └── query.sql

```
Щоб додати CSV файли результатами ЗНО, треба створити директорію "data" та розмістити в ній ці файли.
### Директорія після запуску програми
```
dbis_lab1
├──main.py
├── batches
│   ├── batch_1.csv
│   ├── batch_2.csv
|   |──...
├── data
│   ├── Odata2019File.csv
│   └── Odata2020File.csv
├── logs
│   └── time_log.log
├── main.py
├── query_results
│   └── query_data.csv
├── scripts
│   ├── batches_to_sqltable.py
│   ├── csv_to_batches.py
│   └── small_funcs.py
└── sql_queries
    ├── CREATE.sql
    └── query.sql

```
Файл query_data.csv містить CSV дані до запиту, вказаному за варіантом - дані про середній бал з англійської мови в кожному регіоні. Файл містить рядок - заголовок (Регіон, Середній бал з англійської мови), в наступних рядках приведені відповідно конкретні дані.

Файл time_log.log містить час (в хвилинах та секундах) виконання функціональних блоків програми.
## Запуск програми

Щоб запустити скрипт, треба виконати консольну команду:

```bash
python3 main.py dbname username password host port
```
де після main.py йде перелічення конфігураційних даних для з'єднання з сервером PostgreSQL.
