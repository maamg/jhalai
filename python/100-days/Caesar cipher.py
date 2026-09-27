
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == 'encode':
    encode = ''
    for char in text:
        if char in alphabet:
            encode += alphabet[(alphabet.index(char) + shift) % 26]
        else:
            encode += char
    print(encode.capitalize())
elif direction == 'decode':
    decode = ''
    for char in text:
        if char in alphabet:
            decode += alphabet[(alphabet.index(char) - shift) % 26]
        else:
            decode += char
    print(decode.capitalize())