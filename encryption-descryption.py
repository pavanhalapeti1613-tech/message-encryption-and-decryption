def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# Main program
print("===== Basic Encryption & Decryption =====")

text = input("Enter the text: ")
shift = int(input("Enter the shift key: "))

# Encryption
encrypted_text = encrypt(text, shift)
print("\nEncrypted Text:", encrypted_text)

# Decryption
decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted Text:", decrypted_text)