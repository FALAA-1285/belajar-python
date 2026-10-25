# latihan konversi satuan temperature

# progam konversi suhu dari celcius ke yang lain
print("===Program Konversi Suhu===")
input = float(input("Masukkan suhu dalam Celcius: "))
print("Suhu dalam Celcius: ", input, "°C")

# reamur
reamur = input * 4/5
print("Suhu dalam Reamur: ", reamur, "°R")

# fahrenheit
fahrenheit = (input *9/5)+32
print("Suhu dalam Fahrenheit: ", fahrenheit, "°F")

# kelvin
kelvin = input + 271.15
print("Suhu dalam Kelvin: ", kelvin, "K")