class Fahrenheit:
  def __init__(self, suhu):
    self.suhu = suhu

  def get_fahrenheit(self):
    val = self.suhu
    return val
    
  def get_celcius(self):
    val = (self.suhu - 32) * 5/9
    return val
  
  def get_reamur(self):
    val = (self.suhu - 32) * 4/9
    return val
  
  def get_kelvin(self):
    val = (self.suhu - 32) * 5/9 + 273.15
    return val
 
F = Fahrenheit(60)
val = F.get_fahrenheit()
C = F.get_celcius()
R = F.get_reamur()
K = F.get_kelvin()
print( str(val) + " Fahrenheit, sama dengan:")
print(str(C) + " Celcius")
print(str(R) + " Reamur")
print(str(K) + " Kelvin")