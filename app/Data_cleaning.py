import pandas as pd

from google.colab import files
fake_data = files.upload()

fake_data = pd.read_csv('Fake.csv')
print(fake_data.head())

from google.colab import files
real_data = files.upload()

real_data = pd.read_csv('True.csv')
print(real_data.head())

#data cleaning remove duplicate null etc
fake_data = fake_data.drop_duplicates()
fake_data = fake_data.dropna()
fake_data.dropna(inplace = True)
fake_data = pd.read_csv('Fake.csv')
print(fake_data.head())
fake_data.to_csv('Fake.csv', index=False)

real_data = real_data.drop_duplicates()
real_data = real_data.dropna()
real_data.dropna(inplace = True)
real_data = pd.read_csv('True.csv')
print(real_data.head())
real_data.to_csv('True.csv', index=False)

from google.colab import files
files.download('True.csv')
