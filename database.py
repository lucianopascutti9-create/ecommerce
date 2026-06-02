from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import Depends # Agregado según la captura

# URL de conexión a tu base de datos en Postgres
DATABASE_URL = "postgresql://postgres:lucben2009@localhost:5432/ecommerce_db"

# Creamos el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Fábrica de sesiones corregida
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base sobre la cual heredarán nuestros modelos
Base = declarative_base()

# --- AGREGAR ESTE BLOQUE ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
