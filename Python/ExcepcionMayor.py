class InicialMayorQueFinal(Exception):

    def _init_(self, message="El valor inicial no puede ser mayor que el final o igual."):
        self.message = message