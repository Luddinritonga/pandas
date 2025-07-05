import pandas as pd

data = {'Nama': ['Ali', 'Budi', 'Citra', None],
        'Usia': [25, None, 22, 30],
        'Gaji': [5000000, 7000000, None, 6500000]}

df = pd.DataFrame(data)

# Menghapus baris yang memiliki nilai NaN
df_clean = df.dropna()

# Menghapus kolom yang memiliki nilai NaN
df_clean_cols = df.dropna(axis=1)

print(df_clean)
