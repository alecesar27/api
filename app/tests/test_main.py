import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Teste para cadastrar um produtor rural
def test_cadastrar_produtor_rural():
    response = client.post("/produtores_rurais", json={
        "cpf_cnpj": "18744548923",  # CPF válido
        "area_total_ha": 100,
        "area_agricola_ha": 50,
        "area_vegetacao_ha": 30
    })
    assert response.status_code == 201
    assert response.json()["message"] == "Produtor rural cadastrado com sucesso!"

# Teste para listar todos os produtores
def test_listar_produtores():
    response = client.get("/produtores_rurais")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Verifica se a resposta é uma lista

# Teste para obter um produtor específico
def test_obter_produtor_rural():
    # Primeiro, crie um produtor
    response = client.post("/produtores_rurais", json={
        "cpf_cnpj": "18744548923",
        "area_total_ha": 100,
        "area_agricola_ha": 50,
        "area_vegetacao_ha": 30
    })
    produtor_id = response.json()["id"]

    # Agora, obtenha o produtor
    response = client.get(f"/produtores_rurais/{produtor_id}")
    assert response.status_code == 200
    assert response.json()["cpf_cnpj"] == "18744548923"

# Teste para editar um produtor
def test_editar_produtor_rural():
    # Primeiro, crie um produtor
    response = client.post("/produtores_rurais", json={
        "cpf_cnpj": "18744548923",
        "area_total_ha": 100,
        "area_agricola_ha": 50,
        "area_vegetacao_ha": 30
    })
    produtor_id = response.json()["id"]

    # Agora, edite o produtor
    response = client.put(f"/produtores_rurais/{produtor_id}", json={
        "cpf_cnpj": "12345678909",
        "area_total_ha": 100,
        "area_agricola_ha": 60,  # Alterando a área agrícola
        "area_vegetacao_ha": 20
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Produtor rural atualizado com sucesso!"

# Teste para excluir um produtor
def test_excluir_produtor_rural():
    # Primeiro, crie um produtor
    response = client.post("/produtores_rurais", json={
        "cpf_cnpj": "12345678909",
        "area_total_ha": 100,
        "area_agricola_ha": 50,
        "area_vegetacao_ha": 30
    })
    produtor_id = response.json()["id"]

    # Agora, exclua o produtor
    response = client.delete(f"/produtores_rurais/{produtor_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Produtor rural excluído com sucesso!"

# Teste para obter total de propriedades
def test_total_propriedades():
    response = client.get("/produtores_rurais/total/")
    assert response.status_code == 200
    assert "Total de propriedades" in response.json()

# Teste para obter total de hectares
def test_total_hectares():
    response = client.get("/produtores_rurais/hectares/")
    assert response.status_code == 200
    assert "Total de hectares" in response.json()