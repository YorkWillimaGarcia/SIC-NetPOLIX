# ============================================================
# models.py
# ============================================================

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

connection_string = "postgresql+psycopg2://postgres.himzzqbqzmxrckedqapx:Politecnico123*@aws-1-us-east-1.pooler.supabase.com:6543/postgres"

engine = create_engine(connection_string, echo=False)

SessionLocal = sessionmaker(bind=engine)


class Video(Base):
    __tablename__ = 'Video'

    isan_video       = Column(String, primary_key=True)
    año              = Column(String, nullable=True)
    duracion_minutos = Column(Integer, nullable=True)
    titulo           = Column(String, nullable=True)


class Cliente(Base):
    __tablename__ = "Cliente"

    id_cliente = Column(Integer, primary_key=True)
    cedula     = Column(String, nullable=True)
    nombre     = Column(String, nullable=True)
    apellido   = Column(String, nullable=True)


class Serie(Base):
    __tablename__ = "Serie"

    id_serie   = Column(Integer, primary_key=True)
    nombre     = Column(String, nullable=True)
    temporadas = Column(Integer, nullable=True)


class Categoria(Base):
    __tablename__ = "Categoria"

    id_categoria = Column(Integer, primary_key=True)
    nombre       = Column(String, nullable=True)
    descripcion  = Column(String, nullable=True)


class Idioma(Base):
    __tablename__ = "Idioma"

    id_idioma = Column(Integer, primary_key=True)
    nombre    = Column(String, nullable=True)
    codigo    = Column(String, nullable=True)


try:
    Base.metadata.create_all(engine)
except Exception as e:
    print(f"Advertencia al crear tablas: {e}")