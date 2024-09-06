class ValoresFueraDeLosLimitesException(Exception):

    def __init__(self, message="El valor inicial o valor final no pueden ser mayores que la cantidad de elementos del conjunto"):
        self.message = message

        super().__init__(self.message)