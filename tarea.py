from datetime import datetime

class Tarea:
    
    ESTADO_1 = "PENDIENTE"
    ESTADO_2 = "EN PROGRESO"
    ESTADO_3 = "COMPLETADA"
    
    def __init__(self, identificador, titulo, descripcion, proyecto_asociado, usuario_responsable, fecha_creacion, fecha_finalizacion, estado):
        self.identificador = identificador
        self.titulo = titulo
        self.descripcion = descripcion
        self.proyecto_asociado = proyecto_asociado
        self.usuario_responsable = usuario_responsable
        self.fecha_creacion = fecha_creacion
        self.fecha_finalizacion = fecha_finalizacion
        self.estado = estado
        
    @classmethod
    def crearTarea(cls, identificador, proyecto):
        identificador = identificador;
        proyecto_asociado = proyecto
        titulo = input("Introduce el titulo de la tarea: ")
        descripcion = input("Introduce la descripción: ")
        fecha_creacion = str(datetime.now().strftime("%d-%m-%Y"))
        print(f"Fecha de creación: {fecha_creacion}")
        estado = cls.ESTADO_1
        print(f"Estado actual: {estado}")
        
        usuario_responsable = None
        fecha_finalizacion = None
        
        return cls(identificador, titulo, descripcion, proyecto_asociado, usuario_responsable, fecha_creacion, fecha_finalizacion, estado)
    
    def asignarUsuarioTarea(self, id_usuario):
        self.usuario_responsable = id_usuario
    
    
    def cambiarEstado(self):
        print(f"Tarea: {self.titulo}")
        print(f"Estado actual: {self.estado}")
        print("*********************")
        print("**     ESTADOS     **")
        print("*********************")
        print("** 1. PENDIENTE    **")
        print("** 2. EN PROGRESO  **")
        print("** 3. COMPLETADA   **")
        print("*********************")
        accion = int(input("Selecciona un estado para la tarea: "))
        match accion:
            case 1:
                self.estado = self.ESTADO_1
            case 2:
                self.estado = self.ESTADO_2
            case 3:
                self.estado = self.ESTADO_3
                self.fecha_finalizacion = str(datetime.now().strftime("%d-%m-%Y"))
            case _:
                print("No has seleccionado un estado valido")
        
        