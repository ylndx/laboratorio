class Usuario:
    def __init__ (self, identificador, dni, nombre, apellido):
        self.identificador = identificador
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        
    @classmethod
    def registrarUsuario(cls, identificador):
        dni = input("Introduce el DNI: ")
        nombre = input("Introduce el nombre: ")
        apellido = input("Intrduce el apellido: ")
        
        return cls(identificador, dni, nombre, apellido)