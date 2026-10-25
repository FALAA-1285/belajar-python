# format string 

# contoh generic
# string 
nama = "marlene"
format_str =f"hello: {nama}"
print(format_str)

# angka 
angka = 2005.5
format_str =f"angka: {angka}" 
print(format_str)
# bilangan bulat 
angka = 2005
format_str =f"angka: {angka:d}" 
print(format_str)
# ordo ribuan 
angka = 2000000
format_str = f"angka: {angka:,}"
print(format_str)
# bilangan desimal 
angka = 2005.54321
format_str =f"angka: {angka:.3f}" 
print(format_str)
# menampilkan leading zero 
angka = 2005.54321
format_str =f"angka: {angka:10.3f}" 
print(format_str) 
# menampilkan plus dan minus 
angka_minus = -10
format_str =f"angka: {angka_minus:+d}" 
print(format_str)
angka_plus = 10
format_str =f"angka: {angka_plus:+d}" 
print(format_str)
# memformat persen 
persentase = 0.045
format_str =f"angka: {persentase:.2%}" 
print(format_str)
# melakukan operasi aritmatika di dalam placeholder 
harga = 10000
jumlah = 5
format_str = f"harga total = Rp. {harga*jumlah}"
print(format_str)

# boolean
bool = False
format_str = f"angka: {bool}"
print(format_str)

