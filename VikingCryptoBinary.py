KEYS = {
    'a': '/ᛇ/',
    'b': '/ᛈ/',
    'c': '/ᛉ/',
    'd': '/ᛊ/',
    'e': '/ᛏ/',
    'f': '/ᛒ/',
    'g': '/ᛖ/',
    'h': '/ᛗ/',
    'i': '/ᛚ/',
    'j': '/ᛜ/',
    'k': '/ᛟ/',
    'l': '/ᛞ/',
    'm': '/ᚠ/',
    'n': '/ᚢ/',
    'o': '/ᚦ/',
    'p': '/ᚨ/',
    'q': '/ᚱ/',
    'r': '/ᚲ/',
    's': '/ᚷ/',
    't': '/ᚹ/',
    'u': '/ᚺ/',
    'v': '/ᚾ/',
    'w': '/ᛁ/',
    'x': '/ᛃ/',
    'y': '/ᛗ/',
    'z': '/ᛊ/',
}

def cypher(message):
    words = message.split(" ")
    cypher_message = []

    for word in words:
        cypher_word = " "
                for letter in word:
            cypher_word += KEYS[letter]

        cypher_message.append(cypher_word)

    return " " .join(cypher_message)


def decipher(message):
    words = message.split(" ")
    decipher_message = []

    for word in words:
        decipher_word = " "

        for letter in word:

            for key, value in KEYS.items():
                if value == letter:
                    decipher_word += key

        decipher_message.append(decipher_word)

    return " ".join(decipher_message)


def run():

    while True:

        command = str(input('''--- * --- * --- * --- * --- * --- * --- * ---

            WELCOME TO VIKING CYPHERING What do you want to do?

            [c]ypher message
            [d]ecypher message
            [e]exit
        '''))

        if command == 'c':
            message = str(input("Write your message (lower letters only): "))
            cypher_message = cypher(message)
            print(cypher_message)

        elif command == 'd':
            message = str(input("Write your cyphered message: "))
            decypher_message = decipher(message)
            print(decypher_message)
        elif command == 'e':
            quit()
        else:
            print("¡That's an invalid choice!")


if __name__ == '__main__':
    print('M E N S A J E S  C I F R A D O S')
    run()