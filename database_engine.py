from sqlalchemy import create_engine, Column, String, Float, Integer, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
import datetime

Base = declarative_base()

# 1. TABLA DE SOCIOS (Tenants)
class Tenant(Base):
    __tablename__ = 'tenants'
    id = Column(String, primary_key=True) # ej: 'oasis_animal'
    name = Column(String, nullable=False) # ej: 'Oasis Animal'
    schema_type = Column(String, default='B2B') # B2B, B2C o Interno

# 2. TABLA DE PRODUCTOS (Vinculados a un socio)
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    tenant_id = Column(String, ForeignKey('tenants.id'))
    sku = Column(String, unique=True) # Código único
    name = Column(String, nullable=False)
    base_cost = Column(Float) # Costo de material + tiempo
    price_x3 = Column(Float)  # Precio final sugerido (Alejandra)

# Configuración inicial para SQLite local
engine = create_engine('sqlite:///elpasaje_v2.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

print("✅ Cerebro del sistema (DB) inicializado correctamente.")
