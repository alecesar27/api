from sqlalchemy import Column, Integer, String
from .database import Base
from pydantic import BaseModel

class ProdutorRural(Base):
    __tablename__ = 'produtores_rurais'

    id = Column(Integer, primary_key=True)
    cpf_cnpj = Column(String, nullable=False, unique=True)
    nome_produtor = Column(String, nullable=False)
    nome_fazenda = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    estado = Column(String, nullable=False)
    area_total_ha = Column(Integer, nullable=False)
    area_agricola_ha = Column(Integer, nullable=False)
    area_vegetacao_ha = Column(Integer, nullable=False)
    culturas_plantadas = Column(String, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'cpf_cnpj':self.cpf_cnpj, 
            'nome_produtor':self.nome_produtor, 
            'nome_fazenda':self.nome_fazenda, 
            'cidade':self.cidade,
            'estado':self.estado, 
            'area_total_ha':self.area_total_ha,
            'area_agricola_ha':self.area_agricola_ha,
            'area_vegetacao_ha':self.area_vegetacao_ha,
            'culturas_plantadas' :self.culturas_plantadas         
        }

class ProdutorRuralCreate(BaseModel):
    cpf_cnpj: int
    nome_produtor: str
    nome_fazenda: str
    cidade: str
    estado: str
    area_total_ha: int
    area_agricola_ha: int
    area_vegetacao_ha: int
    culturas_plantadas: str
