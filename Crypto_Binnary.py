def code(texto):
    binario = ' '.join(format(x, 'b') for x in bytearray(texto,'UTF-8'))
    return binario

def decode(binario):
    mensaje = binario.split(' ')
    texto = ''.join(chr(int(x,base=2)) for x in mensaje)
    return texto

def run():

    mensaje = ''

    while(True):

        opcion = str(input('''
        ••••••••••••••••••••••••••••••••••••••••••••••
        C   R   Y   P   T   O   G   R   A   P   H   Y
        ••••••••••••••••••••••••••••••••••••••••••••••
        Choose an option:
                        [C]ode
                        [D]ecode
                        [E]xit

        ''').upper())

        if(opcion == 'C'):
            encrypted = code(input('Message to code: '))
            print(encrypted)
        elif(opcion == 'D'):
            unencrypted = decode(input('Message to decode: '))
            print(' ')
            print(unencrypted)
        elif (opcion == 'E'):
            quit()
        else:
            print('Choose a valid option')

if __name__ == '__main__':
    run()