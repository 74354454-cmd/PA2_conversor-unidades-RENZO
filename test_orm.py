import pytest
from sqlalchemy import create_engine
from database import Base, Conversion, get_session, init_db

def test_guardar_conversion_orm():
    # Creamos BD en memoria para la prueba unitaria
    engine = create_engine("sqlite:///:memory:")
    init_db(engine)
    session = get_session(engine)
    
    # Implementación de mapeo objeto-relacional
    nueva_conv = Conversion(
        tipo="peso", 
        funcion="kg_to_libras", 
        valor_entrada=10.0, 
        valor_salida=22.05
    )
    session.add(nueva_conv)
    session.commit()
    
    # Validación del flujo ORM
    resultado = session.query(Conversion).first()
    assert resultado.valor_salida == 22.05