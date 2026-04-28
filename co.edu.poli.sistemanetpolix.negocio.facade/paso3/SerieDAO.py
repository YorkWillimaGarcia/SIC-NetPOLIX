# ============================================================
# SerieDAO.py
# ============================================================

from models import Serie, SessionLocal
from sqlalchemy.orm import Session


class SerieDAO:

    def __init__(self, db_session: Session):
        self.db = db_session

    def crear(self, id_serie, nombre, temporadas):
        nueva_serie = Serie(
            id_serie   = id_serie,
            nombre     = nombre,
            temporadas = temporadas
        )
        self.db.add(nueva_serie)
        self.db.commit()
        self.db.refresh(nueva_serie)
        return nueva_serie

    def obtener_todos(self):
        return self.db.query(Serie).all()

    def obtener_por_id(self, id_serie):
        return self.db.query(Serie).filter(Serie.id_serie == id_serie).first()

    def actualizar(self, id_serie, nuevo_nombre, nuevas_temporadas):
        serie = self.obtener_por_id(id_serie)
        if serie:
            serie.nombre     = nuevo_nombre
            serie.temporadas = nuevas_temporadas
            self.db.commit()
        return serie

    def eliminar(self, id_serie):
        serie = self.obtener_por_id(id_serie)
        if serie:
            self.db.delete(serie)
            self.db.commit()
        return True