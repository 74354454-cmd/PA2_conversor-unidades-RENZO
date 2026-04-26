from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# Esta es la línea que te falta o está mal escrita:
Base = declarative_base()

class Conversion(Base):
    __tablename__ = "conversiones"
    id = Column(Integer, primary_key=True)
    tipo = Column(String, nullable=False)
    funcion = Column(String, nullable=False)
    valor_entrada = Column(Float, nullable=False)
    valor_salida = Column(Float, nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow)

def get_engine(db_url="sqlite:///conversiones.db"):
    return create_engine(db_url)

def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()

def init_db(engine):
    Base.metadata.create_all(engine)