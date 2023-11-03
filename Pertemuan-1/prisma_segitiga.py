print("Program menghitung luas dan volume prisma segitiga")
"""
Programmer :
Pertemuan : 1
Tanggal : 22 Oktober 2023
"""
# Nilai
alas = 3
tinggi = 6
luas = 8
tinggiprisma = 10
sisi1 = 6
sisi2 = 7
sisi3 = 8

# Rumus mengitung luas alas prisma segitiga
luasalas =(sisi1+sisi2+sisi3)*tinggiprisma

# Rumus mengitung luas sisi prisma segitiga
luassisi = (sisi1+sisi2+sisi3)*tinggiprisma+alas*tinggi

# Rumus mengitung volume prisma segitiga
volume = (alas*tinggi)/2*tinggiprisma

# Output
print("Alas :",alas)
print("Tinggi :",tinggi)
print("Luas :",luas)
print("Sisi1 :",sisi1)
print("Sisi2 :",sisi2)
print("Sisi3 :",sisi3)
print("Luas Alas :",luasalas)
print("Luas Sisi :",luassisi)
print("Volume :",volume)