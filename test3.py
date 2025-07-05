import pandas as pd

# Membuat MultiIndex DataFrame
arrays = [
    ['A', 'A', 'B', 'B'],
    ['Satu', 'Dua', 'Satu', 'Dua']
]

index = pd.MultiIndex.from_tuples(list(zip(*arrays)), names=['Huruf', 'Angka'])

data = pd.DataFrame({'Nilai': [10, 20, 30, 40]}, index=index)

print(data)
