# ============================================================
# ClienteDAO.py
# Capa de acceso a datos (DAO) para la entidad Cliente
# ============================================================

from models import Cliente, SessionLocal
from sqlalchemy.orm import Session


class ClienteDAO:

    def __init__(self, db_session: Session):
        self.db = db_session

    # --------------------------------------------------------
    # Método: crear
    # Inserta un nuevo cliente en la base de datos
    # --------------------------------------------------------
    def crear(self):
        print("\n=== CREAR CLIENTE ===")
        while True:
            nuevo_cliente = Cliente(
                id_cliente = int(input("\nDigite el ID del cliente: ")),
                cedula     = input("Digite la cédula: "),
                nombre     = input("Digite el nombre: "),
                apellido   = input("Digite el apellido: ")
            )
            self.db.add(nuevo_cliente)
            self.db.commit()
            self.db.refresh(nuevo_cliente)
            print("Registro insertado exitosamente.")

            var = input("\n¿Desea agregar otro cliente?\n1. Sí \n2. No\n")
            if var != "1":
                break
        return nuevo_cliente

    # --------------------------------------------------------
    # Método: obtener_todos
    # Recupera todos los registros de la tabla Cliente
    # --------------------------------------------------------
    def obtener_todos(self):
        print("\n=== TODOS LOS CLIENTES ===")
        clientes = self.db.query(Cliente).all()
        if not clientes:
            print("No hay registros.")
        else:
            for c in clientes:
                print(f"ID: {c.id_cliente} | Cédula: {c.cedula} | Nombre: {c.nombre} | Apellido: {c.apellido}")
        return clientes

    # --------------------------------------------------------
    # Método: obtener_por_id
    # Busca un cliente por su clave primaria
    # --------------------------------------------------------
    def obtener_por_id(self):
        print("\n=== BUSCAR CLIENTE POR ID ===")
        while True:
            id_cliente  = input("\nDigite el ID del cliente: ")
            cur_cliente = self.db.query(Cliente).filter(Cliente.id_cliente == id_cliente).first()

            if cur_cliente is None:
                print("Cliente no encontrado.")
            else:
                print(f"ID: {cur_cliente.id_cliente} | Cédula: {cur_cliente.cedula} | Nombre: {cur_cliente.nombre} | Apellido: {cur_cliente.apellido}")

            var = input("\n¿Desea buscar otro cliente?\n1. Sí \n2. No\n")
            if var != "1":
                break

    # --------------------------------------------------------
    # Método: actualizar
    # Modifica los datos de un cliente existente
    # --------------------------------------------------------
    def actualizar(self):
        print("\n=== ACTUALIZAR CLIENTE ===")
        while True:
            id_cliente  = input("\nIngrese el ID del cliente a actualizar: ")
            cur_cliente = self.db.query(Cliente).filter(Cliente.id_cliente == id_cliente).first()

            if cur_cliente is None:
                print("Cliente no encontrado.")
            else:
                while True:
                    print("\n¿Qué información desea actualizar?\n1. Cédula\n2. Nombre\n3. Apellido")
                    upd = input()

                    if upd == "1":
                        cur_cliente.cedula = input("Ingrese la nueva cédula: ")
                    elif upd == "2":
                        cur_cliente.nombre = input("Ingrese el nuevo nombre: ")
                    elif upd == "3":
                        cur_cliente.apellido = input("Ingrese el nuevo apellido: ")
                    else:
                        print("Opción no válida.")

                    self.db.commit()
                    self.db.refresh(cur_cliente)
                    print("Registro actualizado exitosamente.")

                    var = input("\n¿Desea actualizar otro dato del cliente?\n1. Sí \n2. No\n")
                    if var != "1":
                        break

            var = input("\n¿Desea actualizar otro cliente?\n1. Sí \n2. No\n")
            if var != "1":
                break

    # --------------------------------------------------------
    # Método: eliminar
    # Elimina un cliente de la base de datos por su ID
    # --------------------------------------------------------
    def eliminar(self):
        print("\n=== ELIMINAR CLIENTE ===")
        while True:
            id_cliente  = input("Digite el ID del cliente a eliminar: ")
            cur_cliente = self.db.query(Cliente).filter(Cliente.id_cliente == id_cliente).first()

            if cur_cliente is None:
                print("Cliente no encontrado.")
            else:
                self.db.delete(cur_cliente)
                self.db.commit()
                print("Registro eliminado exitosamente.")

            var = input("\n¿Desea eliminar otro cliente?\n1. Sí \n2. No\n")
            if var != "1":
                break