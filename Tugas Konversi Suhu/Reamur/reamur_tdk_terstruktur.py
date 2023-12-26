print ("Konversi Suhu Reamur")

#Entry
suhu = input("Masukan suhu dalam reamur:")

#rumus
C = (5/4 * float(suhu))
F = (9/4 * float(suhu)) + 32
K = (5/4 * float(suhu)) + 273

#ouput
print(suhu+ " reamur sama dengan ")
print(str(C) + " Celcius ")
print(str(F) + " Fahrenheit ")
print(str(K) + " Kelvin ")
