# ============================================================
# ClienteDAO.py
# Capa de acceso a datos (DAO) para la entidad Cliente
# ============================================================

from models import Cliente, SessionLocal
from sqlalchemy.orm import Session


class ClienteDAO:

    def __init__(self, db_session: Session):
        self.db = db_session

    def crear(self, id_cliente, cedula, nombre, apellido):
        nuevo_cliente = Cliente(
            id_cliente = id_cliente,
            cedula     = cedula,
            nombre     = nombre,
            apellido   = apellido
        )
        self.db.add(nuevo_cliente)
        self.db.commit()
        self.db.refresh(nuevo_cliente)
        return nuevo_cliente

    def obtener_todos(self):
        return self.db.query(Cliente).all()

    def obtener_por_id(self, id_cliente):
        return self.db.query(Cliente).filter(Cliente.id_cliente == id_cliente).first()

    def actualizar(self, id_cliente, nueva_cedula, nuevo_nombre, nuevo_apellido):
        cliente = self.obtener_por_id(id_cliente)
        if cliente:
            cliente.cedula   = nueva_cedula
            cliente.nombre   = nuevo_nombre
            cliente.apellido = nuevo_apellido
            self.db.commit()
        return cliente

    def eliminar(self, id_cliente):
        cliente = self.obtener_por_id(id_cliente)
        if cliente:
            self.db.delete(cliente)
            self.db.commit()
        return True