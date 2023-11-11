def toLowerCase(text):
    return text.lower()

def removeSpaces(text):
    newText = ""
    for i in text:
        if i == " ":
            continue
        else:
            newText = newText + i
    return newText

def Diagraph(text):
    Diagraph = []
    group = 0
    for i in range(2, len(text), 2):
        Diagraph.append(text[group:i])

        group = i
    Diagraph.append(text[group:])
    return Diagraph

def FillerLetter(text):
    k = len(text)
    if k % 2 == 0:
        for i in range(0, k, 2):
            if text[i] == text[i + 1]:
                new_word = text[0:i + 1] + str('x') + text[i + 1:]
                new_word = FillerLetter(new_word)
                break
            else:
                new_word = text
    else:
        for i in range(0, k - 1, 2):
            if text[i] == text[i + 1]:
                new_word = text[0:i + 1] + str('x') + text[i + 1:]
                new_word = FillerLetter(new_word)
                break
            else:
                new_word = text
    return new_word

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def generateKeyTable(word, list1):
    key_letters = []
    for i in word:
        if i not in key_letters:
            key_letters.append(i)

    compElements = []
    for i in key_letters:
        if i not in compElements:
            compElements.append(i)
    for i in list1:
        if i not in compElements:
            compElements.append(i)

    matrix = []
    while compElements != []:
        matrix.append(compElements[:5])
        compElements = compElements[5:]

    return matrix


def search(mat, element):
    for i in range(5):
        for j in range(5):
            if(mat[i][j] == element):
                return i, j


def encrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1c == 4:
        char1 = matr[e1r][0]
    else:
        char1 = matr[e1r][e1c + 1]

    char2 = ''
    if e2c == 4:
        char2 = matr[e2r][0]
    else:
        char2 = matr[e2r][e2c + 1]

    return char1, char2


def encrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1r == 4:
        char1 = matr[0][e1c]
    else:
        char1 = matr[e1r + 1][e1c]

    char2 = ''
    if e2r == 4:
        char2 = matr[0][e2c]
    else:
        char2 = matr[e2r + 1][e2c]

    return char1, char2


def encrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    char1 = matr[e1r][e2c]

    char2 = ''
    char2 = matr[e2r][e1c]

    return char1, char2


def encryptByPlayfairCipher(Matrix, plainList):
    CipherText = []
    for i in range(0, len(plainList)):
        c1 = 0
        c2 = 0
        ele1_x, ele1_y = search(Matrix, plainList[i][0])
        ele2_x, ele2_y = search(Matrix, plainList[i][1])

        if ele1_x == ele2_x:
            c1, c2 = encrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        elif ele1_y == ele2_y:
            c1, c2 = encrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            c1, c2 = encrypt_RectangleRule(
                Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

        cipher = c1 + c2
        CipherText.append(cipher)
    return CipherText

def main():
    while True:
        print("Pilihan:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Keluar")
        choice = input("Pilih tindakan (1/2/3): ")

        if choice == '1':
            text_Plain = input("Masukkan plaintext: ")
            print("Plaintext:", text_Plain)

            text_Plain = removeSpaces(toLowerCase(text_Plain))
            PlainTextList = Diagraph(FillerLetter(text_Plain))
            if len(PlainTextList[-1]) != 2:
                PlainTextList[-1] = PlainTextList[-1] + 'z'

            key = input("Masukkan kata kunci: ")
            print("Kata kunci:", key)
            key = toLowerCase(key)
            key = removeSpaces(key)
            Matrix = generateKeyTable(key, list1)

            CipherList = encryptByPlayfairCipher(Matrix, PlainTextList)

            CipherText = ""
            for i in CipherList:
                CipherText += i
            print("\nHasil Enkripsi:", CipherText)
        elif choice == '2':
            text_Cipher = input("Masukkan ciphertext: ")
            print("Ciphertext:", text_Cipher)

            key = input("Masukkan kata kunci: ")
            print("Kata kunci:", key)
            key = toLowerCase(key)
            key = removeSpaces(key)
            Matrix = generateKeyTable(key, list1)

            decrypted_text = ""
            for i in range(0, len(text_Cipher), 2):
                char1 = text_Cipher[i]
                char2 = text_Cipher[i + 1]
                row1, col1 = search(Matrix, char1)
                row2, col2 = search(Matrix, char2)

                if row1 == row2:
                    char1, char2 = encrypt_RowRule(Matrix, row1, col1, row2, col2)
                elif col1 == col2:
                    char1, char2 = encrypt_ColumnRule(Matrix, row1, col1, row2, col2)
                else:
                    char1, char2 = encrypt_RectangleRule(Matrix, row1, col1, row2, col2)

                decrypted_text += char1 + char2

            print("\nHasil Dekripsi:", decrypted_text)
        elif choice == '3':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

if __name__ == "__main__":
    main()
