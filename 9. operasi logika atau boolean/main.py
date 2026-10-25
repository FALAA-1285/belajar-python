# operasi logika atau boolean

# not, or, and, for

a = True
b = False
print("a:", a)
print("b:", b)
print('\n===NOT===') # akan bernilai kebalikan dari nilai a atau b
print("not a:", not a)
print("not b:", not b)

print('\n===OR===') # akan bernilai True jika a atau b bernilai True, akan bernilai False jika a dan b bernilai False
print("a or b:", a or b)
print("a or True:", a or True)
print("b or False:", b or False)

print('\n===AND===') # akan bernilai True jika a dan b bernilai True, akan bernilai False jika a atau b bernilai False
print("a and b:", a and b)
print("a and True:", a and True)
print("b and False:", b and False)

print('\n===XOR===') # akan bernilai True jika a dan b berbeda, akan bernilai False jika a dan b sama
print("a xor b:", a ^ b)
print("a xor True:", a ^ True)
print("b xor False:", b ^ False)