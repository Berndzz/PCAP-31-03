import pandas as pd

a = ["Cher", "Teknik Sipil", "UK Petra"]

myvar = pd.Series(a, index = ["Nama", "Prodi", "Universitas"])

print(myvar)
