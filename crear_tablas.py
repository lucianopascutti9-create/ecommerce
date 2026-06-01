from database import engine, Base
from models import *

# Levanta todo lo que herede de Base (en este caso Categoria, Producto y Usuario) y lo crea en la DB
Base.metadata.create_all(bind=engine)

print("Tablas creadas correctamente")