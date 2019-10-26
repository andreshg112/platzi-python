def recursive_sum(number):
    if number == 0:
        return 0

    return number + recursive_sum(number - 1)


if __name__ == "__main__":
    number = int(input('''
    Suma un número desde sí mismo hasta cero.
    Por ejemplo: recursive_sum(5) = 5 + 4 + 3 + 2 + 1 = 15
    Ingrese el número:
    '''))

    total = recursive_sum(number)

    print('La suma recursiva es de {}'.format(total))
