# operasi dan manipulasi string

# 1. menyambungkan string (concatenate)
nama_pertama = "Ahmad"
nama_tengah = "D"
nama_akhir = "Falah"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. operator untuk string

# mengecek apakah ada komponen char atau sting di string
# in
d = "d"
status = d in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + " = " + str(status))
# not in
d = "d"
status = d not in nama_lengkap
print("string " + d + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)
print(15*"wk")

# indexing
print("index ke-0 : "+ nama_lengkap[0])
print("index ke-2 : "+ nama_lengkap[2])
print("index ke-5 : "+ nama_lengkap[5])
print("index ke-(1) : "+ nama_lengkap[-1])
print("index ke-[0:3] : "+nama_lengkap[0:3]) # yang terakhir tidak diambil, jadi dari index 0-2
print("index ke-[3:7] : "+nama_lengkap[3:7])

# item paling kecil
print("paling kecil: "+min(nama_lengkap)) 
# item paling besar
print("paling besar: "+max(nama_lengkap))

# 4. operator dalam bentuk method

data = "falahi joko darmono"
jumlah = data.count("o")
print("jumlah o pada '"+ data + "' = "+ str(jumlah))