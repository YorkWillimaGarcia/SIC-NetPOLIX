import ClienteDAO as p  
import VideoDAO as q

def main():
    try:
        #Mostrar al iniciar
        print("\n--- Estado inicial de la base de datos ---")
        p.findAll()

        #Crear Cliente
        print("\n--- Crear nuevo Cliente ---")
        id_nuevo = input("Digite el ID: ")
        cedula = input("Digite la cédula: ")
        nombre = input("Digite el nombre: ")
        apellido = input("Digite el apellido: ")
        
        p.crearPersona(id_nuevo, cedula, nombre, apellido)
        p.findAll()

        #Busqueda por nombre
        print("\n--- Búsqueda ---")
        nombreB = input("Digite el nombre a buscar: ")
        p.buscarPersonaPorNombre(nombreB)

        #Editar
        print("\n--- Editar Cliente ---")
        idU = input("Digite el ID del cliente a actualizar: ")
        cedulaU = input("Digite la nueva cédula: ")
        nombreU = input("Digite el nuevo nombre: ")
        apellidoU = input("Digite el nuevo apellido: ")
        
        p.editarPersona(cedulaU, nombreU, apellidoU, idU)
        p.findAll()

        #Elimminar
        print("\n--- Borrar Cliente ---")
        idE = input("Digite el ID del cliente a eliminar: ")
        p.eliminarPersona(idE)
        
        print("\n--- Estado final de la base de datos ---")
        p.findAll()

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()