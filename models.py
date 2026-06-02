from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Categoria(Base):
    __tablename__ = "categorias"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    
    # Mapea con la relación en Producto usando "categorias" en plural
    productos = relationship("Producto", back_populates="categorias")


class Producto(Base):
    __tablename__ = "productos"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    precio = Column(Float)
    en_stock = Column(Boolean, default=True)
    
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    
    # Cambiado a plural 'categorias' con back_populates="productos" según el documento
    categorias = relationship("Categoria", back_populates="productos")


class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)





    