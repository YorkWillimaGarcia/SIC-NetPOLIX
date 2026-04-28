# ============================================================
# VideoDAO.py
# Capa de acceso a datos (DAO) para la entidad Video
# ============================================================

from models import Video, SessionLocal
from sqlalchemy.orm import Session


class VideoDAO:

    def __init__(self, db_session: Session):
        self.db = db_session

    def crear(self, isan_video, titulo, año, duracion_minutos):
        nuevo_video = Video(
            isan_video       = isan_video,
            titulo           = titulo,
            año              = año,
            duracion_minutos = duracion_minutos
        )
        self.db.add(nuevo_video)
        self.db.commit()
        self.db.refresh(nuevo_video)
        return nuevo_video

    def obtener_todos(self):
        return self.db.query(Video).all()

    def obtener_por_isan(self, isan_video):
        return self.db.query(Video).filter(Video.isan_video == isan_video).first()

    def obtener_por_titulo(self, titulo):
        return self.db.query(Video).filter(Video.titulo.ilike(f"%{titulo}%")).all()

    def actualizar(self, isan_video, nuevo_titulo, nuevo_año, nueva_duracion):
        video = self.obtener_por_isan(isan_video)
        if video:
            video.titulo           = nuevo_titulo
            video.año              = nuevo_año
            video.duracion_minutos = nueva_duracion
            self.db.commit()
        return video

    def eliminar(self, isan_video):
        video = self.obtener_por_isan(isan_video)
        if video:
            self.db.delete(video)
            self.db.commit()
        return True
        