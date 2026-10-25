# string

data = "ini adalah string" # kumpulan karakter
print(data, type(data))

# 1. cara membuat string

'''
    1. menggunakan sigle quote
    2. menggunakan double quote
'''

data = "menggunakan singgle qoute" 
print(data)


data = "menggunakan double qoute" 
print(data)

print("'hallo, apa kabar ?'")
print('"hallo, apa kabar ?"')
print("ini adalah hari jum'at")

# 2. menggunakan tanda |

# membuat tanda ' menjadi string
print('mari sholat jum\'at')
print('g\'day, isn\'t it?')

# backslash
print("c:\\user\\falah")

# tab
print("ini\tadalah penggunaakn tab")

# backspace
print("ini dalah penggunaan \bbackspace")

# newline
print("baris pertama.\nbaris kedua.") # line feedd -> linux, macos
print("baris pertama.\rbaris kedua.") # carriage return -> commodore, acorn
print("baris pertama.\r\nbaris kedua.") # line feed carriage return -> windows

# 3. string literal atau raw

# hati-hati
print('C:\new folder') # akan salah pathnya

# menggunakan raw sting
print(r'C:\new folder')

# multiline lateral string and raw
print("""
nama: Falah
kelas: TI/3D
      """)

