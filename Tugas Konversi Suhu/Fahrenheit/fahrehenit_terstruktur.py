print("Konversi suhu fahrenheit")
def get_celcius(suhu):
    C = (5/9 * float(suhu))-32
    return C

def get_reamur(suhu):
    R = (4/9 * float(suhu))-32
    return R

def get_kelvin(suhu):
    K = (5/9 * float(suhu))-32 + 273
    return K

#Entry
suhu = input("Masukan suhu dalam Fahrenheit:")

#rumus
C = get_celcius(suhu)
R = get_reamur(suhu)
K = get_kelvin(suhu)

#output
print(suhu + " fahrenheit sama dengan ")
print(str(C) + " Celcius ")
print(str(R) + " Reamur ")
print(str(K) + " Kelvin ")
