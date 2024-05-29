import pandas as pd
import random
import datetime

num_columns = 5500
num_rows = 17280

column_names = [
    ['','','','','','FOR ONE WELL','','','','',''],
    ['','','','OPC CLIENT DATA FOR ML LEARNING','','','','','','',''],
    ['','','','','Field Instruments', 'MPFM FOR 48/24 HOURS','','','','',''],
    ['DATE&TIME'] + ['X{}'.format(i + 1) for i in range(5)] + ['Y{}'.format(i + 1) for i in range(5)],
    ['D&T', 'DS-PR', 'DS-TS', 'US-PR', 'US-TS', 'CH-FB', 'OIL', 'GAS', 'WATER', 'WATER-CUT', 'GOR']
]

data = []

for i in range(num_rows):
    year = random.randint(2020, 2023)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    date_time = datetime.datetime(year, month, day, hour, minute, second)

    x_values = [random.randint(150, 1000) for _ in range(5)]

    y_values = [random.randint(0, 100) for _ in range(5)]

    data.append([date_time] + x_values + y_values )

df = pd.DataFrame(data, columns=column_names)

df.to_csv('WELL.csv', index=False)
