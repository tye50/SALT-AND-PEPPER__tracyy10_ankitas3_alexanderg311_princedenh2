import pandas as pd

from google.colab import files
fake_data = files.upload()

fake_data = pd.read_csv('Fake.csv')
print(fake_data.head())

#data cleaning remove duplicate null etc
fake_data = fake_data.drop_duplicates()
fake_data = fake_data.dropna()
fake_data.dropna(inplace = True)
fake_data = pd.read_csv('Fake.csv')
print(fake_data.head())
fake_data.to_csv('Fake.csv', index=False)
