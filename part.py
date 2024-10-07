import pandas as pd

df = pd.read_csv('WorldsBestRestaurants.csv')
print(df.head()) # Выводит 5 ячеек информации

data = {
    'Year': [2002, 2002, 2002, 2002, 2002],
    'Restaurant': ['El Bulli', 'Restaurant Gordon Ramsay', 'The French Laundry', 'Rockpool', 'Spoon des Iles'],
    'Country': ['Spain', 'United Kingdom', 'United States', 'Australia', 'Mauritius'],
    'lat': [42.263949, 51.507218, 38.401578, -33.868820, -20.348404],
    'lng': [3.179553, -0.127586, -122.360810, 151.209295, 57.552152]
}
df = pd.DataFrame(data)
print(df)

print(df.info()) # Выводит информацию об файле

print(df.describe()) # Выводит статистические данные

df = pd.read_csv('dz.csv')
average_salary_city = df.groupby('City')['Salary'].mean() # Вычисление средней зарплаты
print(average_salary_city) # Вывод средней зарплаты по городу
