from app.db.models import ProdutorRural, ProdutorRuralCreate
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db.models import Base
from app.db.database import engine


Base.metadata.create_all(bind=engine)

db = SessionLocal()

class ProdutorService:

     
    @staticmethod
    def cadastrar_produtor(produtor: ProdutorRuralCreate):
        try:
            db_produtor = ProdutorRural(**produtor)
            db.add(db_produtor)
            db.commit()
            db.refresh(db_produtor)
        except:
            db.rollback()
            raise ValueError("Erro ao cadastrar produtor, campos obrigatórios ou produtor já cadastrado .")
        return db_produtor

    
    @staticmethod
    def editar_produtor(produtor_id: int, produtor: ProdutorRuralCreate):
        db_produtor = db.query(ProdutorRural).filter(ProdutorRural.id == produtor_id).first()
        if db_produtor is None:
            raise ValueError("Produtor não encontrado") 
        for key, value in produtor.items():
           setattr(db_produtor, key, value)
        db.commit()
        return db_produtor

    @staticmethod
    def excluir_produtor(produtor_id: int):
        db_produtor = db.query(ProdutorRural).filter(ProdutorRural.id == produtor_id).first()
        if db_produtor is None:
            raise ValueError("Produtor não encontrado") 
        db.delete(db_produtor)
        db.commit()
        return {"message": "Produtor excluído com sucesso"}

    @staticmethod
    def listar_produtores():
        return db.query(ProdutorRural).all()

    # @staticmethod
    # def obter_produtor(produtor_id):
    #     produtor = ProdutorRural.query.get(produtor_id)
    #     if not produtor:
    #         raise ValueError("Produtor não encontrado.")
    #     return produtor

    # Endpoint para obter um produtor pelo ID
    @staticmethod
    def obter_produtor(produtor_id: int):
        produtor = db.query(ProdutorRural).filter(ProdutorRural.id == produtor_id).first()
        
        if not produtor:
            raise ValueError("Produtor não encontrado.") 
        
        return produtor