alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").casefold()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        letter_index = alphabet.index(letter)
        shifted_index = letter_index + shift_amount
        while not shifted_index < 26:
            shifted_index -= 26
        cipher_text += alphabet[shifted_index]
    print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text, shift_amount):
    plain_text =""
    for letter in cipher_text:
        letter_index = alphabet.index(letter)
        shifted_index = letter_index - shift_amount
        while not shifted_index >= 0:
            shifted_index += 26
        plain_text += alphabet[shifted_index]
    print(f"The decoded text is {plain_text}")


if direction == 'encode':
    encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
    decrypt(cipher_text=text, shift_amount=shift)