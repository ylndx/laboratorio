from laboratorio.proyecto import Proyecto
from laboratorio.usuario import Usuario
from laboratorio.tarea import Tarea


def main() -> None:
    
    #Declaramos las variables
    cont_usuario = 1
    cont_proyecto = 1
    cont_tarea = 1
    
    #Declaramos las listas donde guardaremos nuestros objetos
    lista_usuarios = []
    lista_proyectos = []
    lista_tareas = []
    
    while True:
    
        # Creamos el menú
        print("********************************************")
        print("**                  MENU                  **")
        print("********************************************")
        print("** 1. Registrar usuario                   **")
        print("** 2. Crear proyectos                     **")
        print("** 3. Crear tarea                         **")
        print("** 4. Asignar tarea a usuario             **")
        print("** 5. Cambiar estado tarea                **")
        print("** 6. Listar tareas de un responsable     **")
        print("** 7. Listar proyectos y tareas asociadas  **")
        print("** 8. Salir                               **")
        print("********************************************")
        accion = int(input("Elige una opción: "))
            
        match(accion):
            case 1:
                print("*************************")
                print("    REGISTRAR USUARIO    ")
                print("*************************")
                usuario = Usuario.registrarUsuario(cont_usuario)
                lista_usuarios.append(usuario)
                cont_usuario += 1
            case 2:
                print("************************")
                print("   CREAR PROYECTO       ")
                print("************************")
                proyecto = Proyecto.crearProyecto(cont_proyecto)
                lista_proyectos.append(proyecto)
                cont_proyecto += 1
                print(f"Total de usuarios creados: {len(lista_usuarios)}")
            case 3:
                print("***********************")
                print("      CREAR TAREA      ")
                print("***********************")
                if(len(lista_proyectos)> 0 and len(lista_usuarios)>0):
                    print("LISTADO DE PROYECTOS:")
                    for p in lista_proyectos:
                        print(f"{p.identificador}. {p.titulo}")
                    proyecto_asociado = int(input("Elige el proyecto al que se asociará la tarea: "))
                    tarea = Tarea.crearTarea(cont_tarea, proyecto_asociado)
                    lista_tareas.append(tarea)
                    cont_tarea += 1
                    print(f"Total de tareas creadas: {len(lista_tareas)}")
                else:
                    print("Debes tener usuarios y proyectos creados para poder crear una tarea")
            case  4:
                print("*******************************")
                print("    ASIGNAR TAREA A USUARIO    ")
                print("*******************************")
                if(len(lista_proyectos)> 0 and len(lista_tareas)>0):
                    print("LISTADO DE TAREAS:")
                    for t in lista_tareas:
                        print(f"{t.identificador}. {t.titulo}")
                    indice_tarea = int(input("Elige una tarea: "))-1
                    tarea_seleccionada = lista_tareas[indice_tarea]
                    print("LISTADO DE USUARIOS:")
                    for u in lista_usuarios:
                        print(f"{u.identificador}. {u.nombre} {u.apellido}")
                    usuario_seleccionado = int(input("Selecciona un usuario para asignarle la tarea: "))
                    tarea_seleccionada.asignarUsuarioTarea(usuario_seleccionado)
                    print(f"La tarea ha sido asiganda a {lista_usuarios[usuario_seleccionado-1].nombre} {lista_usuarios[usuario_seleccionado-1].apellido}")
                else:                    
                    print("Debes tener tareas creadas para poder ejecutar esta opción")
            case 5:
                print("*******************************")
                print("     CAMBIAR ESTADO TAREA      ")
                print("*******************************")
                if(len(lista_proyectos)> 0 and len(lista_tareas)>0):
                    print("LISTADO DE TAREAS:")
                    for t in lista_tareas:
                        print(f"{t.identificador}. {t.titulo}")
                    indice = int(input("Elige una tarea: "))-1
                    tarea_seleccionada = lista_tareas[indice]
                    print(f"tarea: {tarea_seleccionada.titulo}")
                    tarea_seleccionada.cambiarEstado()
                    print(f"El estado se ha cambiado a: {tarea_seleccionada.estado}")
                    
                else:                    
                    print("Debes tener tareas creadas para poder ejecutar esta opción")
            case 6:
                if(len(lista_usuarios)> 0):
                    print("*************************************")
                    print("   LISTAR TAREAS DE UN RESPONSABLE   ")
                    print("*************************************")
                    for u in lista_usuarios:
                        print(f"{u.identificador}. {u.nombre} {u.apellido}")
                    usuario_seleccionado = int(input("Elige un usuario para listar sus tareas: "))
                    print(f"Listado tareas: ")
                    tiene_tareas = False
                    for t in lista_tareas:
                        if t.usuario_responsable == usuario_seleccionado:
                            print(f"{t.identificador}. {t.titulo}")
                            tiene_tareas = True
                    if not tiene_tareas:
                        print("El usuario aún no tiene asignadas tareas")
                else:
                    print("Debes tener usuarios creados para poder ejecutar esta opción")
            case 7:
                print("****************************************")
                print("   LISTAR PROYECTO Y TAREAS ASOCIADAS   ")
                print("****************************************")
                if(len(lista_proyectos)> 0 and len(lista_tareas)>0):
                    for p in lista_proyectos:
                        print(f"{p.identificador}. {p.titulo}: ")
                        for t in lista_tareas:
                            if(t.proyecto_asociado == p.identificador):
                                print(f"    {t.identificador}. {t.titulo} - Estado: {t.estado}")
                        print("-------------")
                else:
                    print("Debes tener proyectos para ejecutar esta opción")
            case 8:
                print ("Hasta pronto...")
                break #Rompemos el bucle y termina
            case _:
                print("No es una opción valida")
        


if __name__ == "__main__":
    main()    
    