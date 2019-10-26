def code(texto):
    binario = ' '.join(format(x, 'b') for x in bytearray(texto, 'UTF-8'))

    return binario


def decode(binario):
    mensaje = binario.split(' ')

    texto = ''.join(chr(int(x, base=2)) for x in mensaje)

    return texto


def run():
    while True:
        opcion = str(input('''
        ••••••••••••••••••••••••••••••••••••••••••••••
        C   R   I   P   T   O   G   R   A   F   I   A
        ••••••••••••••••••••••••••••••••••••••••••••••
        Seleccione una opción:
                        [C]odificar
                        [D]ecodificar
                        [S]alir

        ''').upper())

        if(opcion == 'C'):
            encrypted = code(input('Mensaje a codificar:'))

            print(encrypted)
        elif(opcion == 'D'):
            unencrypted = decode(input('Mensaje a decodificar: '))

            print(' ')

            print('El mensaje original es: ', unencrypted)
        else:
            break


if __name__ == '__main__':
    run()
