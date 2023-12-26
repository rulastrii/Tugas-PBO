print("Konversi suhu kelvin")
def get_celcius(suhu):
    C = (float(suhu))- 273
    return C

def get_fahrenheit(suhu):
    F = (9/5 * float(suhu)) - 273 + 32
    return F

def get_reamur(suhu):
    R = (4/5 * float(suhu)) - 273
    return R

#Entry
suhu = input("Masukan suhu dalam Kelvin:")

#rumus
C = get_celcius(suhu)
F = get_fahrenheit(suhu)
R = get_reamur(suhu)

#ouput
print(suhu+ " kelvin sama dengan ")
print(str(C) + " Celcius ")
print(str(F) + " Fahrenheit ")
print(str(R) + " Reamur ")
