"""
Take text from input: any text
change each letter:
"""
x = input("Get text: ")
result = ''
previous = ''

for letter in x:
    if previous == '':
        previous = letter
        result = result + letter
    else:
        l = chr(ord(letter)+ord(previous))
        result = result + l
        previous = letter

print(result)
k = x[0]

result2 = k
for letter in result[1:]:
    new_k = chr(ord(letter) - ord(k))
    result2 += new_k
    k = new_k

print(result2)