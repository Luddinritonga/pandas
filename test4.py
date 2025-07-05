#Contoh membaca CSV dan menyimpannya kembali
#pip install openpyxl

import pandas as pd

# Membaca file CSV
df = pd.read_csv('data1.csv')

# Menampilkan 5 baris pertama
print(df.head())

# Menyimpan kembali ke format lain (misalnya Excel)
df.to_excel('data.xlsx', index=False)
