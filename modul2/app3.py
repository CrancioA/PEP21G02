"""
Get text from input: abc #defg
return: ace...
"""
x = input("Get text: ")

z1 = chr(ord(x[0]) + (ord(x[0]) - ord('a')))
z2 = chr(ord(x[1]) + (ord(x[1]) - ord('a')))
z3 = chr(ord(x[2]) + (ord(x[2]) - ord('a')))
z4 = chr(ord(x[3]) + (ord(x[3]) - ord('a')))
z5 = chr(ord(x[4]) + (ord(x[4]) - ord('a')))
z6 = chr(ord(x[5]) + (ord(x[5]) - ord('a')))
z7 = chr(ord(x[6]) + (ord(x[6]) - ord('a')))
print(f'{z1}{z2}{z3}{z4}{z5}{z6}{z7}')
