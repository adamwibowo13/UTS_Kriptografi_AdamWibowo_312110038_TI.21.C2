def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_length = len(key)
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char.lower()) - ord('a')
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char.lower()) - ord('a')
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    return decrypted_text

while True:
    print("Pilihan:")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar")

    choice = input("Masukkan pilihan (1/2/3): ")

    if choice == '1':
        plain_text = input("Masukkan pesan yang akan dienkripsi: ")
        key = input("Masukkan kunci: ")
        encrypted_text = vigenere_encrypt(plain_text, key)
        print("Pesan Terenkripsi:", encrypted_text)
    elif choice == '2':
        encrypted_text = input("Masukkan pesan terenkripsi: ")
        key = input("Masukkan kunci: ")
        decrypted_text = vigenere_decrypt(encrypted_text, key)
        print("Pesan Terdekripsi:", decrypted_text)
    elif choice == '3':
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")