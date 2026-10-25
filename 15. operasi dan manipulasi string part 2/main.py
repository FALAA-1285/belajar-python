# operator dalam bentuk methods

## merubah case dari string

# merubah semua ke upper case

salam = "bro!"
print("nurmal = "+salam)
salam = salam.upper()
print("upper = "+salam)

# merubah semua ke lower case
alay = "aKu KeCe AbieezZzZZzzz"
print("normal = "+alay)
alay= alay.lower()
print("lower = "+alay)

## pengecekan dengan isX method

# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya boolean
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + " is upper = " + str(apakah_upper))

# 1. isalpha() -> Mengecek apakah semuanya huruf[cite: 1]
kata1 = "Ahmad"
apakah_alpha = kata1.isalpha()
print(kata1 + " is alpha = " + str(apakah_alpha))

kata2 = "Ahmad Falah"
apakah_alpha = kata2.isalpha()
print(kata2 + " is alpha = " + str(apakah_alpha))

kata3 = "Ahmad123"
apakah_alpha = kata3.isalpha()
print(kata3 + " is alpha = " + str(apakah_alpha))


# isalnum() -> Mengecek huruf dan angka[cite: 1]
data1 = "Ahmad123"
apakah_alnum = data1.isalnum()
print(data1 + " is alnum = " + str(apakah_alnum))

data2 = "Ahmad 123"
apakah_alnum = data2.isalnum()
print(data2 + " is alnum = " + str(apakah_alnum))


# isdecimal() -> Mengecek angka saja[cite: 1]
angka1 = "2026"
apakah_decimal = angka1.isdecimal()
print(angka1 + " is decimal = " + str(apakah_decimal))

angka2 = "20.26"
apakah_decimal = angka2.isdecimal()
print(angka2 + " is decimal = " + str(apakah_decimal))


# isspace() -> Mengecek spasi, tab, newline[cite: 1]
spasi1 = "   "
apakah_space = spasi1.isspace()
print("'" + spasi1 + "' is space = " + str(apakah_space))

spasi2 = " a "
apakah_space = spasi2.isspace()
print("'" + spasi2 + "' is space = " + str(apakah_space))


# istitle() -> Mengecek semua kata dimulai huruf besar[cite: 1]
judul1 = "Ahmad D Falah"
apakah_title = judul1.istitle()
print(judul1 + " is title = " + str(apakah_title))

judul2 = "Ahmad d Falah"
apakah_title = judul2.istitle()
print(judul2 + " is title = " + str(apakah_title))

judul3 = "AHMAD FALAH"
apakah_title = judul3.istitle()
print(judul3 + " is title = " + str(apakah_title))
## Cek komponen dengan startswith() dan endswith()

kalimat = "Sangjangnim Oppa"

# 1. startswith() -> Mengecek apakah diawali kata tertentu
cek_start = kalimat.startswith("Sangjangnim")
print("start = " + str(cek_start)) # Hasil: True

cek_start_salah = kalimat.startswith("sangjangnim") # huruf 's' kecil
print("start (s kecil) = " + str(cek_start_salah)) # Hasil: False


# 2. endswith() -> Mengecek apakah diakhiri kata tertentu
cek_end = kalimat.endswith("Oppa")
print("end = " + str(cek_end)) # Hasil: True

cek_end_salah = kalimat.endswith("Oppak")
print("end (Oppak) = " + str(cek_end_salah)) # Hasil: False


## Penggabungan komponen: join() dan split()

# join() -> Menggabungkan list menjadi string
pisah = ['aku', 'sayang', 'kamu']
print("data list = " + str(pisah))

# digabung menggunakan koma
gabung_koma = ','.join(pisah)
print("gabung koma = " + gabung_koma)
# digabung menggunakan spasi
gabung_spasi = ' '.join(pisah)
print("gabung spasi = " + gabung_spasi)
# digabung menggunakan kata " ehm "
gabung_ehm = ' ehm '.join(pisah)
print("gabung ehm = " + gabung_ehm)


# split() -> Memecah string kembali menjadi list
kalimat = "aku ehm sayang ehm kamu"
# dipecah berdasarkan kata " ehm "
pecah_ehm = kalimat.split(' ehm ')
print("hasil split ehm = " + str(pecah_ehm))
# jika split() dikosongkan, otomatis memecah berdasarkan spasi
kalimat_biasa = "Ahmad D Falah"
pecah_spasi = kalimat_biasa.split()
print("hasil split spasi = " + str(pecah_spasi))

## Alokasi karakter: rjust(), ljust(), center(), dan strip()

# 1. rjust() -> Rata kanan dengan total 10 karakter
kanan = "kanan".rjust(10)
print("'" + kanan + "'")

# 2. ljust() -> Rata kiri dengan total 10 karakter
kiri = "kiri".ljust(10)
print("'" + kiri + "'")

# 3. center() -> Rata tengah dengan total 10 karakter (diisi spasi)
tengah = "tengah".center(10)
print("'" + tengah + "'")

# center() dengan karakter pengisi khusus (misalnya tanda '-' sepanjang 20 karakter)
tengah_strip = "tengah".center(20, "-")
print("'" + tengah_strip + "'")


# 4. strip() -> Menghilangkan karakter pengisi atau spasi di pinggir
# menghilangkan tanda '-' dari variabel tengah_strip
bersih_strip = tengah_strip.strip("-")
print("'" + bersih_strip + "'")

# menghilangkan spasi dari variabel kanan
bersih_spasi = kanan.strip()
print("'" + bersih_spasi + "'")