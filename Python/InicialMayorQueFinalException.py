class InicialMayorQueFinal(Exception):

    def __init__(self, message="El valor inicial no puede ser mayor que el final."):
        self.message = message

        super().__init__(self.message)
