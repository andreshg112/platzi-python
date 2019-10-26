class Medicine:
    ''' Clase Medicina '''

    def __init__(self, name, quantity):
        '''
        Constructor de la clase Medicina
        @parameter str:name
        @parameter int:quantity
        '''

        self.name = name

        self.quantity = quantity

    def take(self, amount):
        '''
        Función que recibe la cantidad de medicina a tomar
        y retorna la cantidad restante.
        @parameter int:amount
        '''

        if amount > self.quantity:
            raise ValueError(
                'La cantidad a tomar de {} es mayor que la existente {}.'
                .format(self.name, self.quantity)
            )

        self.quantity -= amount


if __name__ == "__main__":
    name = str(input('Ingrese el nombre de la medicina: '))

    quantity = int(input('Ingrese la cantidad inicial: '))

    medicine = Medicine(name, quantity)

    while medicine.quantity > 0:
        amount = int(input('Ingrese la cantidad a tomar: '))

        try:
            medicine.take(amount)

            print('Quedan {} de {}'.format(medicine.quantity, medicine.name))
        except ValueError as identifier:
            print(identifier)
