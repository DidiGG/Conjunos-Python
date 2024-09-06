class InicialMayorQueFinal(Exception):

    def __init__(self, message="El valor inicial no puede ser mayor que el final o igual."):
        self.message = message

        super().__init__(self.message)
