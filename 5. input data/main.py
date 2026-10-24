# input dari user
data = input("masukkan data: ") #data yang dimasukkan akan selalu bertipe string
print("data = ", data, ", bertipe = ", type(data)) 

# input data integer
data_int = int(input("masukkan angka: ")) #data yang dimasukkan akan diubah menjadi integer
print("data = ", data_int, ", bertipe = ", type(data_int))

# input data float
data_float = float(input("masukkan angka desimal: ")) #data yang dimasukkan akan diubah menjadi float
print("data = ", data_float, ", bertipe = ", type(data_float))

# input data boolean
data_bool = bool(int(input("masukkan boolean (0/1): "))) #data yang dimasukkan akan diubah menjadi boolean
print("data = ", data_bool, ", bertipe = ", type(data_bool))