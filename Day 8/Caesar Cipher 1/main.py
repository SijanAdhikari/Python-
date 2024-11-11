alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def encrypt(original_text,shift_amount):
    index_with_shift=0
    final_encrypt=""
    for letters in original_text :
        index=alphabet.index(letters)
        index_with_shift=index+shift_amount
        index_with_shift=index_with_shift % len(alphabet)
        letter=alphabet[index_with_shift]
        final_encrypt+=letter
        #above line 15 can be written as follows:
        # if index_with_shift>=26:
        #     index_with_shift-=26
        #     letter=alphabet[index_with_shift]
        #     final_encrypt+=letter
        # else:
        #     letter=alphabet[index_with_shift]
        #     final_encrypt+=letter
    print(final_encrypt)


if direction=="encode":
    encrypt(text,shift)


