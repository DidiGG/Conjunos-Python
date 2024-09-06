class ValoresFueraDeLosLimitesException(Exception):

    def _init_(self, message="El valor inicial o valor final no pueden ser mayores que la cantidad de elementos del conjunto"):
        self.message = message

        super()._init_(self.message)