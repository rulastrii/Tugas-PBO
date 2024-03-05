print("Konversi suhu reamur")
def get_celcius(suhu):
    C = (5/4 * float(suhu))
    return C

def get_fahrenheit(suhu):
    F = (9/4 * float(suhu)) + 32
    return F

def get_kelvin(suhu):
    K = (5/4 * float(suhu)) + 273
    return K

#Entry
suhu = input("Masukan suhu dalam Reamur:")

#rumus
C = get_celcius(suhu)
F = get_fahrenheit(suhu)
K = get_kelvin(suhu)

#ouput
print(suhu+ " reamur sama dengan ")
print(str(C) + " Celcius ")
print(str(F) + " Fahrenheit ")
print(str(K) + " Kelvin ")
