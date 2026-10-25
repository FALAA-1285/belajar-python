# latihan komparasi dan logika

inputUser= int(input("Masukkan angka yang bernilai kurang dari 3 atau lebih dari 10: "))
# membuat gabungan area rentangan angka
# ++++++3------10+++++
print("\n=== gabungan area rentangan angka ===")
# memerika apakah input user kurang dari 3
isKurangDariTiga = inputUser < 3
print("Kurang dari tiga: ", isKurangDariTiga)

# memerika apakah input user lebih dari 10
isLebihDariSepuluh = inputUser > 10
print("Lebih dari sepuluh: ", isLebihDariSepuluh)

# gabungan area rentangan angka
isKurangDariTigaAtauLebihDariSepuluh = isKurangDariTiga or isLebihDariSepuluh
print("Gabungan area rentangan angka: ", isKurangDariTigaAtauLebihDariSepuluh)

# membuat irisan area rentangan angka
# ------3++++++10------
print("\n=== irisan area rentangan angka ===")
# memerika apakah input user lebih dari 3
isLebihDariTiga = inputUser > 3
print("Lebih dari tiga: ", isLebihDariTiga)

# memerika apakah input user kurang dari 10
isKurangDariSepuluh = inputUser < 10
print("Kurang dari sepuluh: ", isKurangDariSepuluh)

# irisan area rentangan angka
isLebihDariTigaDanKurangDariSepuluh = isLebihDariTiga and isKurangDariSepuluh
print("Irisan area rentangan angka: ", isLebihDariTigaDanKurangDariSepuluh)