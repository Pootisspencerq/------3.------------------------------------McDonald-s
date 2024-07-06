import pandas as pd 
#місце для твого коду
df = pd.read_csv('menu.csv')
df.info() 
mean_tfat = df['total fat '].mean()
print(mean_tfat)