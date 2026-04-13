# ============================================================
# models.py
# Define la conexión a la base de datos y el modelo Persona
# mapeado a la tabla 'persona' en MySQL
# ============================================================

from sqlalchemy import create_engine,Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError

# Base declarativa de SQLAlchemy
Base = declarative_base()

# Conexión a MySQL
#connection_string = "mysql+mysqlconnector://root:psswrd@localhost:3306/agenda"
connection_string = "postgresql+psycopg2://postgres.himzzqbqzmxrckedqapx:Politecnico123*@aws-1-us-east-1.pooler.supabase.com:6543/postgres"

# Motor
engine = create_engine(connection_string, echo=True)

# Fábrica de sesiones
SessionLocal = sessionmaker(bind=engine)


"""def getConnection():
    try:
        return SessionLocal()
    except SQLAlchemyError as e:
        print(f"No se puede conectar a la base de datos: {e}")
        return None


def unconnection(session):
    if session:
        session.close()"""


# ------------------------------------------------------------
# Clase: Persona
# Representa un registro de la tabla 'persona' en la base de datos
#
# Atributos:
#   idpersona     (int)  -- Clave primaria
#   nombre        (str)  -- Nombre de la persona
#   apellido      (str)  -- Apellido de la persona
#   email         (str)  -- Correo electrónico
#   num_documento (str)  -- Número de documento de identidad
#
# Ejemplo:
#   p = Persona(idpersona=1, nombre="Ana", apellido="García",
#               email="ana@mail
"""class Persona(Base):
    __tablename__ = 'persona'

    idpersona     = Column(Integer, primary_key=True)
    nombre        = Column(String, nullable=True)
    apellido      = Column(String, nullable=True)
    email         = Column(String, nullable=True)
    num_documento = Column(String, nullable=True)
"""
class Video(Base):
    __tablename__ = 'Video'

    isan_video = Column(String, primary_key=True)
    año = Column(String, nullable=True)
    duracion_minutos = Column(Integer, nullable=True)
    titulo = Column(String, nullable=True)


class Cliente(Base):
    __tablename__ = "Cliente"

    id_cliente = Column(Integer, primary_key=True)
    cedula = Column(String, nullable=True)
    nombre = Column(String, nullable=True)
    apellido = Column(String, nullable=True)




# Crea las tablas en la BD si no existen aún
Base.metadata.create_all(engine)


