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


def caesar(mode, input_text, shift_amount):
    new_text = ""
    for letter in input_text:
        position = alphabet.index(letter)
        if mode == "encode":
            shifted_index = position + shift_amount
            while not shifted_index < 26:
                shifted_index -= 26
        elif mode == "decode":
            shifted_index = position - shift_amount
            while not shifted_index >= 0:
                shifted_index += 26
        new_text += alphabet[shifted_index]
    print(f"The {mode}d text is {new_text}")


caesar(mode=direction, input_text=text, shift_amount=shift)
