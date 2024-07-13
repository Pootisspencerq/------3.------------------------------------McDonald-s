import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних з файлу
file_path = 'menu.csv'
data = pd.read_csv(file_path)

# Видалення пустих рядків
cleaned_data = data.dropna(how='all')

# Збереження очищених даних у новий файл
cleaned_file_path = 'cleaned_menu.csv'
cleaned_data.to_csv(cleaned_file_path, index=False)

# Побудова графіку середньої калорійності страв за категоріями
average_calories_by_category = cleaned_data.groupby('Category')['Calories'].mean().sort_values()

# Налаштування графіку
plt.figure(figsize=(12, 8))
average_calories_by_category.plot(kind='barh', color='skyblue')
plt.xlabel('Середня калорійність')
plt.ylabel('Категорія')
plt.title('Середня калорійність страв за категоріями')

# Збереження графіку у файл
plot_file_path = 'average_calories_by_category.png'
plt.savefig(plot_file_path)

# Відображення графіку
plt.show()

# Перевірка наявності стовпця 'Calories' та обчислення середньої калорійності
if 'Calories' in cleaned_data.columns:
    average_calories = cleaned_data['Calories'].mean()
    print(f"Середня калорійність страв: {average_calories:.2f} ккал")
else:
    print("Стовпець 'Calories' не знайдено в таблиці.")

# Перевірка наявності стовпців для БЖУ та обчислення їх співвідношення
if all(x in cleaned_data.columns for x in ['Protein', 'Total Fat', 'Carbohydrates']):
    cleaned_data['protein_ratio'] = cleaned_data['Protein'] / (cleaned_data['Protein'] + cleaned_data['Total Fat'] + cleaned_data['Carbohydrates'])
    cleaned_data['fat_ratio'] = cleaned_data['Total Fat'] / (cleaned_data['Protein'] + cleaned_data['Total Fat'] + cleaned_data['Carbohydrates'])
    cleaned_data['carbs_ratio'] = cleaned_data['Carbohydrates'] / (cleaned_data['Protein'] + cleaned_data['Total Fat'] + cleaned_data['Carbohydrates'])

    print("\nСпіввідношення БЖУ:")
    print(cleaned_data[['Item', 'protein_ratio', 'fat_ratio', 'carbs_ratio']].head())
else:
    print("Одного зі стовпців 'Protein', 'Total Fat' або 'Carbohydrates' не знайдено в таблиці.")

# Перевірка наявності стовпців для мікроелементів та обчислення їх середнього значення
micronutrients = ['Iron (% Daily Value)', 'Calcium (% Daily Value)', 'Vitamin C (% Daily Value)']
if all(x in cleaned_data.columns for x in micronutrients):
    average_micronutrients = cleaned_data[micronutrients].mean()
    print("\nСередній вміст корисних мікроелементів (у відсотках від добової норми):")
    print(average_micronutrients)
else:
    print("Одного зі стовпців 'Iron (% Daily Value)', 'Calcium (% Daily Value)' або 'Vitamin C (% Daily Value)' не знайдено в таблиці.")
