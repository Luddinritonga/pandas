import pandas as pd

data = {
    'Nama': ['Ali', 'Budi', 'Citra'],
    'Usia': [25, 30, 22],
    'Kota': ['Jakarta', 'Bandung', 'Surabaya']
}

df = pd.DataFrame(data)

print(df)
