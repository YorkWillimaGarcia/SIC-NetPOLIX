# ============================================================
# IdiomaDAO.py
# ============================================================

from models import Idioma, SessionLocal
from sqlalchemy.orm import Session


class IdiomaDAO:

    def __init__(self, db_session: Session):
        self.db = db_session

    def crear(self, id_idioma, nombre, codigo):
        nuevo_idioma = Idioma(
            id_idioma = id_idioma,
            nombre    = nombre,
            codigo    = codigo
        )
        self.db.add(nuevo_idioma)
        self.db.commit()
        self.db.refresh(nuevo_idioma)
        return nuevo_idioma

    def obtener_todos(self):
        return self.db.query(Idioma).all()

    def obtener_por_id(self, id_idioma):
        return self.db.query(Idioma).filter(Idioma.id_idioma == id_idioma).first()

    def actualizar(self, id_idioma, nuevo_nombre, nuevo_codigo):
        idioma = self.obtener_por_id(id_idioma)
        if idioma:
            idioma.nombre = nuevo_nombre
            idioma.codigo = nuevo_codigo
            self.db.commit()
        return idioma

    def eliminar(self, id_idioma):
        idioma = self.obtener_por_id(id_idioma)
        if idioma:
            self.db.delete(idioma)
            self.db.commit()
        return True