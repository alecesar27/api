
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.services.produtor_service import ProdutorService
from app.utils import Util


router = APIRouter()

@router.post("/produtores_rurais")
async def cadastrar_produtor_rural(data: dict):
    try:
        # Validar CPF ou CNPJ
        if 'cpf_cnpj' in data and len(Util.remover_caracteres_cpf(data['cpf_cnpj'])) <= 11 and not Util.validar_cpf(data['cpf_cnpj']):
            raise HTTPException(status_code=400, detail='CPF inválido.')
        if 'cpf_cnpj' in data and len(Util.remover_caracteres_cnpf(data['cpf_cnpj'])) >= 14 and not Util.validar_cnpj(data['cpf_cnpj']):
            raise HTTPException(status_code=400, detail='CPF ou CNPJ inválido.')
       
        # Validar Soma áreas
        if not Util.validar_AreaTotal(data['area_total_ha'],data['area_agricola_ha'],data['area_vegetacao_ha']):
            raise HTTPException(status_code=400, detail='A soma da Área Agrícola mais a Área de Vegetação deve ser menor ou igual à Área Total.')
        
        produtor = ProdutorService.cadastrar_produtor(data)
        return JSONResponse(content={'message': 'Produtor rural cadastrado com sucesso!', 'id': produtor.id}, status_code=201)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.put("/produtores_rurais/{produtor_id}")
async def editar_produtor_rural(produtor_id: int, data: dict):
    try:
        # Validar CPF ou CNPJ
        if 'cpf_cnpj' in data and len(data['cpf_cnpj']) <= 11 and not Util.validar_cpf(data['cpf_cnpj']):
            raise HTTPException(status_code=400, detail='CPF inválido.')
        if 'cpf_cnpj' in data and len(data['cpf_cnpj']) >= 14 and not Util.validar_cnpj(data['cpf_cnpj']):
            raise HTTPException(status_code=400, detail='CPF ou CNPJ inválido.')
                # Validar Soma áreas
        if not Util.validar_AreaTotal(data['area_total_ha'],data['area_agricola_ha'],data['area_vegetacao_ha']):
            raise HTTPException(status_code=400, detail='A soma da Área Agrícola mais a Área de Vegetação deve ser menor ou igual à Área Total.')

        produtor = ProdutorService.editar_produtor(produtor_id, data)
        return JSONResponse(content={'message': 'Produtor rural atualizado com sucesso!', 'id': produtor.id}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/produtores_rurais/{produtor_id}")
async def excluir_produtor_rural(produtor_id: int):
    try:
        ProdutorService.excluir_produtor(produtor_id)
        return JSONResponse(content={'message': 'Produtor rural excluído com sucesso!'}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/produtores_rurais")
async def listar_produtores():
    try:
        produtores = ProdutorService.listar_produtores()
        return JSONResponse(content=[produtor.to_dict() for produtor in produtores], status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/produtores_rurais/{produtor_id}")
async def obter_produtor_rural(produtor_id: int):
    try:
        produtor = ProdutorService.obter_produtor(produtor_id)
        return JSONResponse(content=produtor.to_dict(), status_code=200)
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/produtores_rurais/total/")
async def total_propriedades():
    try:
        produtores = ProdutorService.listar_produtores()
        
        total={
           'Total de propriedades':Util.total_propriedades(produtores)
         }
        return JSONResponse(content=total, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/produtores_rurais/hectares/")
async def total_hectares():
    try:
        produtores = ProdutorService.listar_produtores()
        total={
           'Total de hectares':Util.total_hectares(produtores)
        }
        return JSONResponse(content=total, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    