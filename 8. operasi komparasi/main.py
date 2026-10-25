# operasi komparasi

# setiap opearasi komparasi akan menghasilkan nilai boolean True atau False

"""
    >  : lebih besar dari
    <  : lebih kecil dari   
    >= : lebih besar dari atau sama dengan
    <= : lebih kecil dari atau sama dengan
    == : sama dengan
    != : tidak sama dengan    
"""
a = 4

# lebih besar dari (>)
hasil = a > 3
print(a, ">", 3, ": ", hasil)

# lebih kecil dari (<)
hasil = a < 3
print(a, "<", 3, ": ", hasil)

# lebih besar dari atau sama dengan (>=)
hasil = a >= 4
print(a, ">=", 4, ": ", hasil)
hasil = a >= 5
print(a, ">=", 5, ": ", hasil)

# lebih kecil dari atau sama dengan (<=)
hasil = a <= 4
print(a, "<=", 4, ": ", hasil)
hasil = a <= 3
print(a, "<=", 3, ": ", hasil)

# sama dengan (==)
hasil = a == 4
print(a, "==", 4, ": ", hasil)
hasil = a == 5
print(a, "==", 5, ": ", hasil)

# tidak sama dengan (!=)
hasil = a != 4
print(a, "!=", 4, ": ", hasil)
hasil = a != 5
print(a, "!=", 5, ": ", hasil)

# 'is' sebagai komparasi object identity
x = 5
y = 5
z = 7
hasil = x is y
print(x, "is", y, ": ", hasil)
hasil = x is z
print(x, "is", z, ": ", hasil)
hasil = x is not z
print(x, "is not", z, ": ", hasil)
hasil = x is not y
print(x, "is not", y, ": ", hasil)
# nilai id() sama jika object sama, berbeda jika object berbeda
print("nilai x: ", x, ", id: ", id(x))
print("nilai y: ", y, ", id: ", id(y))
print("nilai z: ", z, ", id: ", id(z))