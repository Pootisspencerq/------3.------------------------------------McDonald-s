import pandas as pd

# Завантаження даних з файлу CSV
data = pd.read_csv('menu.csv')

# Вивід перших кількох рядків таблиці
print("Перші кілька рядків таблиці:")
print(data.head())

# Вивід назв стовпців
print("\nНазви стовпців:")
print(data.columns)

# Огляд загальної інформації про дані
print("\nЗагальна інформація:")
print(data.info())

# Підрахунок середньої калорійності
if 'Calories' in data.columns:
    average_calories = data['Calories'].mean()
    print(f"\nСередня калорійність страв: {average_calories:.2f} ккал")
else:
    print("\nСтовпець 'Calories' не знайдено в таблиці.")

# Підрахунок співвідношення БЖУ
if all(x in data.columns for x in ['Protein', 'Total Fat', 'Carbohydrates']):
    data['protein_ratio'] = data['Protein'] / (data['Protein'] + data['Total Fat'] + data['Carbohydrates'])
    data['fat_ratio'] = data['Total Fat'] / (data['Protein'] + data['Total Fat'] + data['Carbohydrates'])
    data['carbs_ratio'] = data['Carbohydrates'] / (data['Protein'] + data['Total Fat'] + data['Carbohydrates'])

    print("\nСпіввідношення БЖУ:")
    print(data[['Item', 'protein_ratio', 'fat_ratio', 'carbs_ratio']])
else:
    print("\nОдного зі стовпців 'Protein', 'Total Fat' або 'Carbohydrates' не знайдено в таблиці.")

# Середній вміст корисних мікроелементів
micronutrients = ['Iron (% Daily Value)', 'Calcium (% Daily Value)', 'Vitamin C (% Daily Value)']
if all(x in data.columns for x in micronutrients):
    average_micronutrients = data[micronutrients].mean()
    print("\nСередній вміст корисних мікроелементів (у відсотках від добової норми):")
    print(average_micronutrients)
else:
    print("\nОдного зі стовпців 'Iron (% Daily Value)', 'Calcium (% Daily Value)' або 'Vitamin C (% Daily Value)' не знайдено в таблиці.")
