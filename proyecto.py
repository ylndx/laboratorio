from datetime import datetime

class Proyecto:
    def __init__(self, identificador, titulo, fecha_creacion, fecha_entrega):
        self.identificador = identificador
        self.titulo = titulo
        self.fecha_creacion = fecha_creacion
        self.fecha_entrega = fecha_entrega
        
    @classmethod
    def crearProyecto(cls, identificador):
        identificador = identificador
        titulo = input("Introduce el titulo del proyecto: ")
        fecha_creacion = str(datetime.now().strftime("%d-%m-%Y"))
        print(f"Fecha creacion: {fecha_creacion}")
        fecha_entrega = input('Introduce la fecha en la que debe ser entregado el proyecto: (Formato "dd-mm-aa"): ')
        return cls(identificador, titulo, fecha_creacion, fecha_entrega)
    
        
