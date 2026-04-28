# ============================================================
# CategoriaDAO.py
# ============================================================

from models import Categoria, SessionLocal
from sqlalchemy.orm import Session


class CategoriaDAO:

    def __init__(self, db_session: Session):
        self.db = db_session

    def crear(self, id_categoria, nombre, descripcion):
        nueva_categoria = Categoria(
            id_categoria = id_categoria,
            nombre       = nombre,
            descripcion  = descripcion
        )
        self.db.add(nueva_categoria)
        self.db.commit()
        self.db.refresh(nueva_categoria)
        return nueva_categoria

    def obtener_todos(self):
        return self.db.query(Categoria).all()

    def obtener_por_id(self, id_categoria):
        return self.db.query(Categoria).filter(Categoria.id_categoria == id_categoria).first()

    def actualizar(self, id_categoria, nuevo_nombre, nueva_descripcion):
        categoria = self.obtener_por_id(id_categoria)
        if categoria:
            categoria.nombre      = nuevo_nombre
            categoria.descripcion = nueva_descripcion
            self.db.commit()
        return categoria

    def eliminar(self, id_categoria):
        categoria = self.obtener_por_id(id_categoria)
        if categoria:
            self.db.delete(categoria)
            self.db.commit()
        return True