alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesar(original_text, shift_amount, direction):
    end_text = ""
    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "encode":
                new_position = (position + shift_amount) % len(alphabet)
            elif direction == "decode":
                new_position = (position - shift_amount) % len(alphabet)
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {direction} text is: {end_text}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(original_text=text, shift_amount=shift, direction=direction)