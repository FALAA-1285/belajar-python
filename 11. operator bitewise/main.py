# operator bitwise / operasi biner
# or, and, xor, not
a = 9
b =5
print('nilai a:', a, ', binary:', format(a, '08b'))
print('nilai b:', b, ', binary:', format(b, '08b'))

# bitwise or (|)
print("\n===OR===")
c = a | b
print('a | b:', c, ', binary:', format(c, '08b'))

# bitwise and (&)
print("\n===AND===")
c = a & b
print('a & b:', c, ', binary:', format(c, '08b'))

# bitwise xor (^)
print("\n===XOR===")
c = a ^ b
print('a ^ b:', c, ', binary:', format(c, '08b'))

# bitwise not (~)
print("\n===NOT===")
c = ~a
print('~a:', c, ', binary:', format(c, '08b'))

# shifting

# shift right
print("\n===SHIFT RIGHT===")
c = a >> 2
print('a >> 2:', c, ', binary:', format(c, '08b'))

# shift left
print("\n===SHIFT LEFT===")
c = a << 2
print('a << 2:', c, ', binary:', format(c, '08b'))