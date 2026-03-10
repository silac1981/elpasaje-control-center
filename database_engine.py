from sqlalchemy import create_engine, Column, String, Float, Integer, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

Base = declarative_base()

# 📘 1. MODELO DE SOCIOS (Tenants)
class Tenant(Base):
    __tablename__ = 'tenants'
    id = Column(String, primary_key=True)  # ej: 'oasis_animal', 'pharma_delux'
    name = Column(String, nullable=False)
    schema_type = Column(String, default='B2B')

# 📦 2. MODELO DE PRODUCTOS
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    tenant_id = Column(String, ForeignKey('tenants.id'))
    sku = Column(String, unique=True)
    name = Column(String, nullable=False)
    base_cost = Column(Float)  # Costo material + tiempo
    price_x3 = Column(Float)   # Precio sugerido Alejandra

# 💰 3. MODELO DE ÓRDENES (Ventas/Pedidos)
class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    tenant_id = Column(String, ForeignKey('tenants.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, default=1)
    total_price = Column(Float)
    status = Column(String, default='Pendiente')
    created_at = Column(DateTime, default=datetime.utcnow)

# 🚀 4. INICIALIZACIÓN DE LA BASE DE DATOS
# (Se pone al final para que reconozca todos los modelos anteriores)
engine = create_engine('sqlite:///elpasaje_v2.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":
    print("✅ Arquitectura de Datos: 100% Operativa y Sincronizada.")