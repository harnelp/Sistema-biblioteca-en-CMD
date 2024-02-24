from biblioteca import Biblioteca
import persistencia

def main():
    biblioteca = persistencia.cargar_datos() or Biblioteca()

    while True:
        print("")
        accion = input("""Ingrese una acción (
            ################################################
            ***Selecciona un número según sea tu elección***
            ################################################
            1: agregar libro, 2: mostrar libros, 3: registrar usuarios, 
            4: prestar, 5: devolver, 6: listar usuarios, 
            7: Listar Libros de Usuario, 8: salir,
            *** Ingresa 'cancelar' en cualquier momento para volver al menú ***
            ): """).strip().lower()

        # Convertir acción numérica a palabra clave si es necesario
        accion = {
            "1": "agregar",
            "2": "mostrar",
            "3": "registrar",
            "4": "prestar",
            "5": "devolver",
            "6": "listar-usuarios",
            "7": "listar-libros-y-usuario",
            "8": "salir"
        }.get(accion, accion)

        if accion == "cancelar":
            continue

        if accion == "salir":
            persistencia.guardar_datos(biblioteca)
            print("Saliendo del sistema...")
            break
        elif accion == "agregar":
            titulo = input("Título del libro (o ingresa 'cancelar' para volver): ")
            if titulo.lower() == "cancelar": continue
            autor = input("Autor del libro (o ingresa 'cancelar' para volver): ")
            if autor.lower() == "cancelar": continue
            cantidad_str = input("Cantidad de libros (o ingresa 'cancelar' para volver): ")
            if cantidad_str.lower() == "cancelar": continue
            try:
                cantidad = int(cantidad_str)
                biblioteca.agregar_libro(titulo, autor, cantidad)
            except ValueError:
                print("Por favor, ingrese un número válido para la cantidad.")

        elif accion == "mostrar":
            biblioteca.mostrar_libros()
        elif accion == "registrar":
            nombre = input("Nombre del usuario: ")
            biblioteca.registrar_usuario(nombre)
        elif accion == "prestar":
            nombre_usuario = input("Nombre del usuario: ")
            titulo = input("Título del libro: ")
            biblioteca.prestar_libro(titulo, nombre_usuario)
        elif accion == "devolver":
            nombre_usuario = input("Nombre del usuario: ")
            titulo = input("Título del libro: ")
            biblioteca.devolver_libro(titulo, nombre_usuario)
        elif accion == "listar-usuarios":
            biblioteca.listar_usuarios()
        elif accion == "listar-libros-y-usuario":
            nombre_usuario = input("Nombre del usuario: ")
            biblioteca.listar_libros_usuario(nombre_usuario)
        else:
            print("Opción no reconocida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
