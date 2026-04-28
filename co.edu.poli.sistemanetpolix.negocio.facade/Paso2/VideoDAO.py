# ============================================================
# VideoDAO.py
# Capa de acceso a datos (DAO) para la entidad Video
# ============================================================

from models import Video, SessionLocal
from sqlalchemy.orm import Session


class VideoDao:

    def __init__(self, db_session: Session):
        self.db = db_session

    # --------------------------------------------------------
    # Método: crear
    # Inserta un nuevo video en la base de datos
    # --------------------------------------------------------
    def crear(self):
        print("\n=== CREAR VIDEO ===")
        while True:
            nuevo_video = Video(
                isan_video       = input("\nDigite el ISAN del video: "),
                titulo           = input("Digite el título: "),
                año              = input("Digite el año de lanzamiento: "),
                duracion_minutos = int(input("Digite la duración en minutos: "))
            )
            self.db.add(nuevo_video)
            self.db.commit()
            self.db.refresh(nuevo_video)
            print("Registro insertado exitosamente.")

            var = input("\n¿Desea agregar otro video?\n1. Sí \n2. No\n")
            if var != "1":
                break
        return nuevo_video

    # --------------------------------------------------------
    # Método: obtener_todos
    # Recupera todos los registros de la tabla Video
    # --------------------------------------------------------
    def obtener_todos(self):
        print("\n=== TODOS LOS VIDEOS ===")
        videos = self.db.query(Video).all()
        if not videos:
            print("No hay registros.")
        else:
            for v in videos:
                print(f"ISAN: {v.isan_video} | Título: {v.titulo} | Año: {v.año} | Duración: {v.duracion_minutos} min")
        return videos

    # --------------------------------------------------------
    # Método: obtener_por_isan
    # Busca un video por su clave primaria (ISAN)
    # --------------------------------------------------------
    def obtener_por_isan(self):
        print("\n=== BUSCAR VIDEO POR ISAN ===")
        while True:
            isan_video = input("\nIngrese el ISAN del video: ")
            cur_video  = self.db.query(Video).filter(Video.isan_video == isan_video).first()

            if cur_video is None:
                print("Video no encontrado.")
            else:
                print(f"ISAN: {cur_video.isan_video} | Título: {cur_video.titulo} | Año: {cur_video.año} | Duración: {cur_video.duracion_minutos} min")

            var = input("\n¿Desea buscar otro video?\n1. Sí \n2. No\n")
            if var != "1":
                break

    # --------------------------------------------------------
    # Método: obtener_por_titulo
    # Busca videos cuyo título contenga el texto ingresado
    # --------------------------------------------------------
    def obtener_por_titulo(self):
        print("\n=== BUSCAR VIDEO POR TÍTULO ===")
        while True:
            titulo    = input("\nIngrese el título a buscar: ")
            resultados = self.db.query(Video).filter(Video.titulo.ilike(f"%{titulo}%")).all()

            if not resultados:
                print("No se encontraron videos con ese título.")
            else:
                for v in resultados:
                    print(f"ISAN: {v.isan_video} | Título: {v.titulo} | Año: {v.año} | Duración: {v.duracion_minutos} min")

            var = input("\n¿Desea buscar otro título?\n1. Sí \n2. No\n")
            if var != "1":
                break

    # --------------------------------------------------------
    # Método: actualizar
    # Modifica los datos de un video existente
    # --------------------------------------------------------
    def actualizar(self):
        print("\n=== ACTUALIZAR VIDEO ===")
        while True:
            isan_video = input("\nIngrese el ISAN del video a actualizar: ")
            cur_video  = self.db.query(Video).filter(Video.isan_video == isan_video).first()

            if cur_video is None:
                print("Video no encontrado.")
            else:
                while True:
                    print("\n¿Qué información desea actualizar?\n1. Título\n2. Año\n3. Duración")
                    upd = input()

                    if upd == "1":
                        cur_video.titulo = input("Ingrese el nuevo título: ")
                    elif upd == "2":
                        cur_video.año = input("Ingrese el nuevo año: ")
                    elif upd == "3":
                        cur_video.duracion_minutos = int(input("Ingrese la nueva duración en minutos: "))
                    else:
                        print("Opción no válida.")

                    self.db.commit()
                    self.db.refresh(cur_video)
                    print("Registro actualizado exitosamente.")

                    var = input("\n¿Desea actualizar otro dato del video?\n1. Sí \n2. No\n")
                    if var != "1":
                        break

            var = input("\n¿Desea actualizar otro video?\n1. Sí \n2. No\n")
            if var != "1":
                break

    # --------------------------------------------------------
    # Método: eliminar
    # Elimina un video de la base de datos por su ISAN
    # --------------------------------------------------------
    def eliminar(self):
        print("\n=== ELIMINAR VIDEO ===")
        while True:
            isan_video = input("Digite el ISAN del video a eliminar: ")
            cur_video  = self.db.query(Video).filter(Video.isan_video == isan_video).first()

            if cur_video is None:
                print("Video no encontrado.")
            else:
                self.db.delete(cur_video)
                self.db.commit()
                print("Registro eliminado exitosamente.")

            var = input("\n¿Desea eliminar otro video?\n1. Sí \n2. No\n")
            if var != "1":
                break