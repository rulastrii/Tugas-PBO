print("Program menghitung luas dan volume limas segiempat")
"""
Programmer :
Pertemuan : 1
Tanggal : 22 Oktober 2023
"""
# Nilai
sisi = 8
tinggilimas = 10
tinggisegitiga = 12

# Rumus menghitung luas permukaan limas segiempat
luaspermukaan = (sisi*sisi)*tinggilimas
luaspermukaan = (sisi*sisi)+(4*sisi*tinggisegitiga/2)

# Rumus menghitung volume limas segiempat
volume = 1/3*(sisi*sisi)*tinggilimas

# Output
print("Sisi :",sisi)
print("Tiggilimas :",tinggilimas)
print("Tiggisegitiga :",tinggisegitiga)
print("Luas Permukaan :",luaspermukaan)
print("Volume :",volume)