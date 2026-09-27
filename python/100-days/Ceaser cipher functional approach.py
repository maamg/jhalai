alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(message, key):
    encrypted = ''
    for char in message:
        if char in alphabet:
            encrypted += alphabet[(alphabet.index(char)+key) % 26]
        else:
            encrypted += char
    print(encrypted)


def decrypt(message, key):
    decrypted = ''
    for char in message:
        if char in alphabet:
            decrypted += alphabet[(alphabet.index(char) - key)% 26]
        else:
            decrypted += char
    print(decrypted)


if direction == 'encode':
    encrypt(text, shift)

elif direction == 'decode':
    decrypt(text, shift)