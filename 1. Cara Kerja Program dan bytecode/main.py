import time
start_time = time.time()

print("hello")
print("world")

print("hello world")
# ini adalah comment, tidak akaan dieksekusi

a = 10 # ini juga comment, tidak akan dieksekusi
print(a)

""" 
    ini adalah comment multi line, 
    tidak akan dieksekusi 
"""

print(time.time() - start_time, "detik") # ini akan menampilkan waktu eksekusi program

""" 
    kita bisa melakukan compile pada python menggunakan bytecode. 
    cara untuk melakukan compile adalah dengan menggunakan perintah python -m py_compile main.py.
    hasil compile akan tersimpan di folder __pycache__ dengan nama file main.cpython-310.pyc.
"""
 