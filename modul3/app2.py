def enc_dec(text, key):
    result = ''
    for letter in text:
        number = ord(letter)
        # print(chr(number ^ key))
        result += chr(number ^ key)
    return result


output = enc_dec("Hello World", 20500)
print(output)

output_dec = enc_dec(output, 20500)
print(output_dec)