# casting adalah merubah tipe data dari suatu variabel ke tipe data lain. Misalnya, mengubah tipe data integer menjadi string, atau sebaliknya.
# tipe data = int, float, str, bool, complex, list, tuple, set, dict

# Integer
print("\n==== INTEGER ====")
data_int = 10
print("data : ", data_int, " bertipe ", type(data_int))

data_float = float(data_int)
print("data : ", data_float, " bertipe ", type(data_float))

data_str = str(data_int) # akan mengubah angka menjadi string
print("data : ", data_str, " bertipe ", type(data_str))

data_bool = bool(data_int) # akan false jika nilainya 0
print("data : ", data_bool, " bertipe ", type(data_bool))

# float
print("\n==== FLOAT ====")
data_float = 9.9
print("data : ", data_float, " bertipe ", type(data_float))

data_int = int(data_float) # akan dibulatkan ke bawah
print("data : ", data_int, " bertipe ", type(data_int))

data_str = str(data_float) # akan mengubah angka menjadi string
print("data : ", data_str, " bertipe ", type(data_str))

data_bool = bool(data_float) # akan false jika nilainya 0.0
print("data : ", data_bool, " bertipe ", type(data_bool))

# Boolean
print("\n==== BOOLEAN ====")
data_bool = False
print("data : ", data_bool, " bertipe ", type(data_bool))

data_int = int(data_bool) # akan mengubah False menjadi 0 dan True menjadi 1
print("data : ", data_int, " bertipe ", type(data_int))

data_str = str(data_bool) # akan mengubah False menjadi "False" dan True menjadi "True"
print("data : ", data_str, " bertipe ", type(data_str))

data_float = float(data_bool) # akan mengubah False menjadi 0.0 dan True menjadi 1.0
print("data : ", data_float, " bertipe ", type(data_float))

# String
print("\n==== STRING ====")
data_str = "0"
data_text = "falah"
print("data : ", data_str, " bertipe ", type(data_str))
print("data : ", data_text, " bertipe ", type(data_text))

data_int = int(data_str) # akan mengubah string menjadi integer
print("data : ", data_int, " bertipe ", type(data_int))
# data_int = int(data_text) # akan error karena string tidak bisa diubah menjadi integer


data_float = float(data_str) # akan mengubah string menjadi float
print("data : ", data_float, " bertipe ", type(data_float))
# data_float = float(data_text) # akan error karena string tidak bisa diubah menjadi float

data_bool = bool(data_str) # akan mengubah string menjadi boolean, akan false jika string kosong
print("data : ", data_bool, " bertipe ", type(data_bool))
data_bool = bool(data_text) # akan mengubah string menjadi boolean, akan false jika string kosong
print("data : ", data_bool, " bertipe ", type(data_bool))
str_false = ""
data_bool = bool(str_false) # akan mengubah string menjadi boolean, akan false jika string
print("data : ", data_bool, " bertipe ", type(data_bool))