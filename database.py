from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión a tu base de datos en Postgres
DATABASE_URL = "postgresql://postgres:lucben2009@localhost:5432/ecommerce_db"

# Creamos el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Creamos la fábrica de sesiones para interactuar con la DB
# (Corregido el pequeño error tipográfico 'SessionmLocal' de la captura)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base sobre la cual heredarán nuestros modelos de las tablas
Base = declarative_base()



# Base sobre la cual heredarán nuestros modelos de las tablas

# Base sobre la cual heredarán nuestros modelos de las tablas

# Base sobre la cual heredarán nuestros modelos de las tablas
