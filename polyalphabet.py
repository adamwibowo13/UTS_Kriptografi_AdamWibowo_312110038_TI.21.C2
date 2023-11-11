def vigenere_encrypt(plain_text, keys):
    encrypted_text = ""
    key_lengths = [len(key) for key in keys]
    num_keys = len(keys)

    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            key_char = keys[i % num_keys][i % key_lengths[i % num_keys]]
            shift = ord(key_char.lower()) - ord('a')
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text

def vigenere_decrypt(encrypted_text, keys):
    decrypted_text = ""
    key_lengths = [len(key) for key in keys]
    num_keys = len(keys)

    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            key_char = keys[i % num_keys][i % key_lengths[i % num_keys]]
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
        num_keys = int(input("Berapa banyak kunci yang ingin Anda gunakan (1-3): "))
        keys = []
        for i in range(num_keys):
            key = input(f"Masukkan kunci ke-{i + 1}: ")
            keys.append(key)
        encrypted_text = vigenere_encrypt(plain_text, keys)
        print("Pesan Terenkripsi:", encrypted_text)
    elif choice == '2':
        encrypted_text = input("Masukkan pesan terenkripsi: ")
        num_keys = int(input("Berapa banyak kunci yang ingin Anda gunakan (1-3): "))
        keys = []
        for i in range(num_keys):
            key = input(f"Masukkan kunci ke-{i + 1}: ")
            keys.append(key)
        decrypted_text = vigenere_decrypt(encrypted_text, keys)
        print("Pesan Terdekripsi:", decrypted_text)
    elif choice == '3':
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")