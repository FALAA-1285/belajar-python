# tipe data: Angka desimal(integer)
data_integer = 11
print("data : ", data_integer, ", bertipe : ", type(data_integer))

# tipe data: Angka desimal (float)
data_float = 1.5
print("data : ", data_float, ", bertipe : ", type(data_float))

# tipe data: Kumpulan karakter (string)
data_string = "falah"
print("data : ", data_string, ", bertipe : ", type(data_string))

# tipe data: biner true/false (boolean)
data_boolean = False #harus menggunakan huruf kapital pada awal kata True/False
print("data : ", data_boolean, ", bertipe : ",type(data_boolean))

# tipe data khusus

# bilangan kompleks
data_complex = complex(5,6)
print("data : ", data_complex, ", bertipe : ", type(data_complex))

# tipe data dari bahasa C 

from ctypes import c_double, c_char, c_long

data_c_double = c_double(10.5)
print("data : ", data_c_double, ", bertipe : ", type(data_c_double))

data_c_char = c_char(b'a')
print("data : ", data_c_char, ", bertipe : ", type(data_c_char))

data_c_long = c_long(100)
print("data : ", data_c_long, ", bertipe : ", type(data_c_long))