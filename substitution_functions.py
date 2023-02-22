# Caesar Cypher
def encryptCaesar(plaintext):

    # you must also initialize ciphertext as an empty string
    ciphertext = ""

    # let's assume only lowercase letters can be encrypted
    # so we convert plaintext to all lowercase letters just in case
    plaintext = plaintext.lower()

    alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                    'y', 'z', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    listSize = len(alphabetList)
    # print('size of alphabetList= ', listSize)

    for letter in plaintext:
        # print(letter)

        # let's find the position of the letter in our alphabetList array
        indexLetter = alphabetList.index(letter)
        # a good debuggin tool in Python is to print so you can see what you just did
        # print('indexLetter= ', indexLetter)

        # now let's do the shift by 3 modulo total number of letters
        newIndex = (indexLetter + 3) % listSize
        # print('newIndex= ', newIndex)

        # now we go to the alphabetList and find which letter is in the newIndex position
        encryptedLetter = alphabetList[newIndex]
        # print(encryptedLetter)

        # now we append the encrypted letter to the ciphertext
        ciphertext = ciphertext + encryptedLetter
        # print(ciphertext)

    # after we loop through all the letters, we return the ciphertext to the main program
    return ciphertext


def decryptCaesar(ciphertext):
    # here you should add your code
    plaintext = ""

    ciphertext = ciphertext.lower()

    alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                    'y', 'z', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    listSize = len(alphabetList)
    for letter in ciphertext:
        indexLetter = alphabetList.index(letter)
        newIndex = (indexLetter - 3) % listSize
        plaintextLetter = alphabetList[newIndex]
        plaintext = plaintext + plaintextLetter

    return plaintext

# ROT13 encryption


def ROT13(message):
    # here you should add your code
    # print(message)
    output = ""
    shift = 13
    listSize = 26

    alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                    'y', 'z']

    for letter in message:

        if (letter.isalpha()):
            indexLetter = alphabetList.index(letter)
            newIndex = (indexLetter - shift) % listSize
            encryptedLetter = alphabetList[newIndex]
            output = output + encryptedLetter

        else:
            output = output + letter
    return output

# Substitution Box (S-Box)


def sBox(plaintext):
    # here you should add your code
    ciphertext = ""
    alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                    'y', 'z']
    sBoxList = ['c', 'l', 'i', 'm', 'h', 'x', 'e', 'z', 's', 't', 'b', 'p',
                'v', 'o', 'u', 'd', 'r', 'y', 'j', 'q', 'k', 'a', 'g', 'w', 'n', 'f']

    for letter in plaintext:

        if (letter.isalpha()):
            indexLetter = alphabetList.index(letter)
            encryptedLetter = sBoxList[indexLetter]
            ciphertext = ciphertext + encryptedLetter

        else:
            ciphertext = ciphertext + letter

    return ciphertext


def inv_sBox(ciphertext):
    # here you should add your code
    plaintext = ""
    alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                    'y', 'z']
    sBoxList = ['c', 'l', 'i', 'm', 'h', 'x', 'e', 'z', 's', 't', 'b', 'p',
                'v', 'o', 'u', 'd', 'r', 'y', 'j', 'q', 'k', 'a', 'g', 'w', 'n', 'f']

    for letter in ciphertext:

        if (letter.isalpha()):
            indexLetter = sBoxList.index(letter)
            plaintextLetter = alphabetList[indexLetter]
            plaintext = plaintext + plaintextLetter

        else:
            plaintext = plaintext + letter

    return plaintext


if __name__ == '__main__':
    ############# testing #########
    # call the function to encryp here to test (or in your client and server program
    # plaintext = "xray"
    # ciphertext = encryptCaesar(plaintext)
    # print("ciphertext is: ", ciphertext)

    wordArr = ["zoo", "xray", "rellis", "college station", "csci458"]
    print("\n\n")

    # Question 1
    # plaintext = "zoo"
    # ciphertext = encryptCaesar(plaintext)
    # print("plaintext is", plaintext, "ciphertext is", ciphertext)

    # plaintext = "xray"
    # ciphertext = encryptCaesar(plaintext)
    # print("plaintext is", plaintext, "ciphertext is", ciphertext)

    # plaintext = "rellis"
    # ciphertext = encryptCaesar(plaintext)
    # print("plaintext is", plaintext, "ciphertext is", ciphertext)

    # plaintext = "college station"
    # ciphertext = encryptCaesar(plaintext)
    # print("plaintext is", plaintext, "ciphertext is", ciphertext)

    # plaintext = "csci458"
    # ciphertext = encryptCaesar(plaintext)
    # print("plaintext is", plaintext, "ciphertext is", ciphertext)

    # Question 2
    # plaintext = "zoo"
    # print("Before encryption ::", plaintext)
    # ciphertext = encryptCaesar(plaintext)
    # print("After encryption ::", ciphertext)
    # decryptedText = decryptCaesar(ciphertext)
    # print("After decryption ::", decryptedText)

    # Qustion 3

    # for word in wordArr:

    #     plaintext = word
    #     print("Before ROT13 ::", plaintext)

    #     encryptedText = ROT13(plaintext)
    #     print("After ROT13 ::", encryptedText)

    #     encryptedText = ROT13(encryptedText)
    #     print("After ROT13 again::", encryptedText)

    #     print("\n")

    # Question 4

    for word in wordArr:

        plaintext = word
        print("Before sBox ::", plaintext)

        encryptedText = sBox(plaintext)
        print("After sBox ::", encryptedText)

        decryptedText = inv_sBox(encryptedText)
        print("After inv_sBox", decryptedText)

        print("\n")
