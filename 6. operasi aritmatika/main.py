# operasi aritmatika
a = 20
b = -4

# penjumlahan
print("penjumlahan a + b = ", a + b)

# pengurangan
print("pengurangan a - b = ", a - b)

# perkalian
print("perkalian a * b = ", a * b)

# pembagian
print("pembagian a / b = ", a / b)

# pemangkatan
print("pemangkatan a ** b = ", a ** b)

# modulus
print("modulus a % b = ", a % b)

# pembagian bulat
print("pembagian bulat a // b = ", a // b)

# prioritas operasi aritmatika
print("prioritas operasi: ", a + b * a) # perkalian dilakukan terlebih dahulu
print("prioritas operasi: ", (a + b) * a) # operasi dalam kurung dilakukan terlebih dahulu
print("prioritas operasi: ", a ** b * a) # pemangkatan dilakukan terlebih dahulu
print("prioritas operasi: ", a ** (b * a)) # operasi dalam kurung dilakukan terlebih dahulu
print("prioritas operasi: ", a + b / a) # pembagian dilakukan terlebih dahulu
print("prioritas operasi: ", (a + b) / a) # operasi dalam kurung dilakukan terlebih dahulu
print("prioritas operasi: ", a + b // a) # pembagian bulat dilakukan terlebih dahulu

"""
    urutan prioritas operasi aritmatika:
    1. kurung ()
    2. pangkat (**)
    3. perkalian (*), pembagian (/), pembagian bulat (//), modulus (%)
    4. penjumlahan (+), pengurangan (-)
"""