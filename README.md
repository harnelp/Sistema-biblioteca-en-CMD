# Sistema de Gestión de Biblioteca en Python

## Descripción

Este proyecto es un sistema de gestión de biblioteca implementado en Python, diseñado para ser ejecutado a través de la terminal. Permite a los usuarios realizar operaciones básicas de gestión de bibliotecas, como agregar y mostrar libros, registrar usuarios, prestar y devolver libros, listar usuarios y los libros prestados a un usuario específico. Los datos son persistentes entre ejecuciones gracias al uso del módulo `pickle`.

## Estructura del Proyecto

El proyecto se divide en tres archivos principales:

- `main.py`: El punto de entrada de la aplicación. Maneja la interfaz de usuario en la terminal e interactúa con las funcionalidades del sistema de gestión de biblioteca.
- `biblioteca.py`: Contiene las definiciones de las clases `Libro`, `Usuario`, y `Biblioteca`, y la lógica para manejar la adición de libros, el registro de usuarios, el préstamo y la devolución de libros.
- `persistencia.py`: Maneja la carga y guardado de los datos de la biblioteca, permitiendo que el estado de la biblioteca persista entre ejecuciones.

## Funcionalidades

- **Agregar Libro**: Permite añadir un nuevo libro a la biblioteca. Si el libro ya existe, incrementa su cantidad.
- **Mostrar Libros**: Muestra todos los libros disponibles en la biblioteca, incluyendo su autor y cantidad.
- **Registrar Usuario**: Añade un nuevo usuario al sistema.
- **Prestar Libro**: Registra el préstamo de un libro a un usuario, disminuyendo la cantidad disponible del libro.
- **Devolver Libro**: Registra la devolución de un libro por un usuario, incrementando la cantidad disponible del libro.
- **Listar Usuarios**: Muestra una lista de todos los usuarios registrados en el sistema.
- **Listar Libros de Usuario**: Muestra todos los libros que un usuario específico ha prestado.

## Cómo Ejecutar

Para ejecutar el sistema de gestión de biblioteca, asegúrate de tener Python instalado en tu sistema. Luego, sigue estos pasos:

1. Clona o descarga este repositorio en tu sistema local.
2. Abre una terminal o línea de comandos.
3. Navega hasta el directorio donde se encuentra el proyecto.
4. Ejecuta el comando `python main.py`.
5. Sigue las instrucciones en la terminal para interactuar con el sistema.

## Requisitos

- Python 3.x
