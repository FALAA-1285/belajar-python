# latihan konversi satuan temperature

# konversi suhu dari fahrenheit ke kelvin
print("===Program Konversi Suhu===")
fahrenheit_in = float(input("Masukkan suhu dalam Fahrenheit: "))
print("Suhu dalam Fahrenheit: ", fahrenheit_in, "°F")

# konversi ke kelvin
celcius = (fahrenheit_in - 32)*5/9
kelvin = celcius + 273.15
print("suhu dalam kelvin: ", kelvin, "K")

# konversi suhu dari kelvin ke fahrenheit
print("===Program Konversi Suhu===")
kelvin_in = float(input("Masukkan suhu dalam Kelvin: "))
print("Suhu dalam Kelvin: ", kelvin_in, "K")

# konversi kelvin ke fahrenheit
reamur = (kelvin_in - 273) * 4/5
fahrenheit = reamur * 9/4 + 32
print("Suhu dalam Fahrenheit: ", fahrenheit, "°F")