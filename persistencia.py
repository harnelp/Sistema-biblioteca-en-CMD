import pickle

def guardar_datos(biblioteca, archivo='datos_biblioteca.pkl'):
    with open(archivo, 'wb') as f:
        pickle.dump(biblioteca, f)
    print("Datos guardados exitosamente.")

def cargar_datos(archivo='datos_biblioteca.pkl'):
    try:
        with open(archivo, 'rb') as f:
            biblioteca = pickle.load(f)
        print("Datos cargados exitosamente.")
        return biblioteca
    except (FileNotFoundError, EOFError):
        print("Archivo de datos no encontrado, inicializando nueva biblioteca.")
        return None