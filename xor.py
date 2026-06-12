string = "abcd"
result = ""

for char in string:
    # XOR the character with 1
    xor_char = chr(ord(char) ^ 0)
    result += xor_char
print(result)