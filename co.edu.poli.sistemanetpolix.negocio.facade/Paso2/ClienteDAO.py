# ============================================================
# PersonaDAO.py
# Capa de acceso a datos (DAO) para la entidad Persona
# Encapsula todas las operaciones CRUD sobre la tabla 'persona'
# ============================================================

from models import Cliente, SessionLocal
from sqlalchemy.orm import Session


# ------------------------------------------------------------
# Clase: PersonaDAO
# Provee métodos para crear, consultar, actualizar y eliminar
# registros de Persona en la base de datos
#
# Parámetros del constructor:
#   db_session (Session) -- Sesión activa de SQLAlchemy
#
# Ejemplo de uso:
#   session = SessionLocal()
#   dao = PersonaDAO(session)
# ------------------------------------------------------------
class ClienteDAO:

    # Recibe la sesión de base de datos por inyección de dependencias
    def __init__(self, db_session: Session):
        self.db = db_session

    # --------------------------------------------------------
    # Método: crear
    # Inserta una nueva persona en la base de datos
    #
    # Parámetros:
    #   idpersona     (int/str) -- Identificador único
    #   nombre        (str)     -- Nombre de la persona
    #   apellido      (str)     -- Apellido de la persona
    #   email         (str)     -- Correo electrónico
    #   num_documento (str)     -- Número de documento
    #
    # Retorna:
    #   Persona -- El objeto recién creado y persistido
    #
    # Ejemplo:
    #   p = dao.crear(1, "Ana", "García", "ana@mail.com", "123456")
    # --------------------------------------------------------
    def crear(self):
        print("\n=== Crear persona ===")
        nuevo_cliente = Cliente(
            id_cliente =input("\nDigite el ID del cliente: "),
            cedula = input("Digite la cédula: "),
            nombre = input("Digite el nombre: "),
            apellido = input("Digite el apellido: ")
        )
        self.db.add(nuevo_cliente)
        self.db.commit()
        self.db.refresh(nuevo_cliente)  # sincroniza el objeto con los datos de la BD
        return nuevo_cliente

    # --------------------------------------------------------
    # Método: obtener_por_id
    # Busca una persona por su clave primaria
    #
    # Parámetros:
    #   idpersona (int/str) -- ID a buscar
    #
    # Retorna:
    #   Persona | None -- El objeto encontrado o None si no existe
    #
    # Ejemplo:
    #   p = dao.obtener_por_id(1)
    # --------------------------------------------------------
    """def obtener_por_id(self, idpersona):
        return self.db.query(Persona).filter(Persona.idpersona == idpersona).first()

    # --------------------------------------------------------
    # Método: obtener_por_nombre
    # Busca la primera persona que coincida con el nombre dado
    #
    # Parámetros:
    #   nombre (str) -- Nombre exacto a buscar
    #
    # Retorna:
    #   Persona | None -- El objeto encontrado o None si no existe
    #
    # Ejemplo:
    #   p = dao.obtener_por_nombre("Ana")
    # --------------------------------------------------------
    def obtener_por_nombre(self, nombre):
        return self.db.query(Persona).filter(Persona.nombre == nombre).first()

    # --------------------------------------------------------
    # Método: obtener_todos
    # Recupera todos los registros de la tabla persona
    #
    # Retorna:
    #   list[Persona] -- Lista de objetos Persona (puede ser vacía)
    #
    # Ejemplo:
    #   personas = dao.obtener_todos()
    #   for p in personas:
    #       print(p.nombre)
    # --------------------------------------------------------
    def obtener_todos(self):
        return self.db.query(Persona).all()

    # --------------------------------------------------------
    # Método: actualizar
    # Modifica los datos de una persona existente
    #
    # Parámetros:
    #   idpersona             (int/str) -- ID de la persona a modificar
    #   nuevo_nombre          (str)     -- Nuevo nombre
    #   nuevo_apellido        (str)     -- Nuevo apellido
    #   nuevo_email           (str)     -- Nuevo correo electrónico
    #   nuevo_num_documento   (str)     -- Nuevo número de documento
    #
    # Retorna:
    #   Persona | None -- El objeto actualizado, o None si no se encontró
    #
    # Ejemplo:
    #   p = dao.actualizar(1, "Ana", "López", "ana2@mail.com", "654321")
    # --------------------------------------------------------
    def actualizar(self, idpersona, nuevo_nombre, nuevo_apellido, nuevo_email, nuevo_num_documento):
        persona = self.obtener_por_id(idpersona)
        if persona:
            persona.nombre        = nuevo_nombre
            persona.apellido      = nuevo_apellido
            persona.email         = nuevo_email
            persona.num_documento = nuevo_num_documento
            self.db.commit()
        return persona

    # --------------------------------------------------------
    # Método: eliminar
    # Elimina una persona de la base de datos por su ID
    #
    # Parámetros:
    #   idpersona (int/str) -- ID de la persona a eliminar
    #
    # Retorna:
    #   bool -- True si se eliminó (o si no existía)
    #
    # Ejemplo:
    #   resultado = dao.eliminar(1)
    # --------------------------------------------------------
    def eliminar(self, idpersona):
        persona = self.obtener_por_id(idpersona)
        if persona:
            self.db.delete(persona)
            self.db.commit()
        return True"""