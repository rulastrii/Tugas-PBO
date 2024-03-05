print("Program menghitung luas dan volume kerucut")
"""
Programmer :
Pertemuan : 1
Tanggal : 22 Oktober 2023
"""
# Nilai
jarijari = 6
sisi = 8
tinggi = 10
phi = 22/7

# Rumus mengitung luas selimut kerucut
luasselimut = phi*jarijari*sisi

# Rumus mengitung luas permukaan kerucut
luaspermukaan = 2*phi*jarijari*sisi+2*phi*jarijari**2

# Rumus mengitung volume kerucut
volume = 1/3*phi*jarijari**2*tinggi

# Output
print("Jari Jari :",jarijari)
print("Sisi :",sisi)
print("Tinggi :",tinggi)
print("Phi :",phi)
print("Luas Selimut :",luasselimut)
print("Luas Permukaan :",luaspermukaan)
print("Volume :",volume)