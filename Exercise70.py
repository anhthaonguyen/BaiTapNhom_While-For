message = input("Nhap thong diep ma hoa: ")
shift = int(input("Nhap so luong: "))

encoded_message = ""
for char in message:
    if char.isalpha():
        if char.isupper():
            encoded_char = chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encoded_char = chr((ord(char) - 97 + shift) % 26 + 97)
        encoded_message += encoded_char
    else:
        encoded_message += char

print("Thong diep ma hoa:", encoded_message)
