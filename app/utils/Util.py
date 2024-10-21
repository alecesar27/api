import re

def validar_cpf(cpf):
    # Remover caracteres não numéricos
    cpf = re.sub(r'\D', '', cpf)
    
    # Verificação de CPF com 11 dígitos
    if len(cpf) != 11 or cpf == cpf[0] * len(cpf):
        return False

    # Cálculo do dígito verificador
    def calcular_digito(cpf, peso):
        soma = sum(int(d) * peso for d, peso in zip(cpf[:-1], range(peso, 1, -1)))
        digito = 11 - (soma % 11)
        return str(digito) if digito < 10 else '0'

    # Validação dos dois últimos dígitos
    return cpf[-2:] == (calcular_digito(cpf, 10) + calcular_digito(cpf, 11))

def validar_cnpj(cnpj):
    # Remover caracteres não numéricos
    cnpj = re.sub(r'\D', '', cnpj)
    
    # Verificação de CNPJ com 14 dígitos
    if len(cnpj) != 14 or cnpj == cnpj[0] * len(cnpj):
        return False

    # Cálculo do dígito verificador
    def calcular_digito(cnpj, peso):
        soma = sum(int(d) * peso for d, peso in zip(cnpj[:-2], peso))
        digito = 11 - (soma % 11)
        return str(digito) if digito < 10 else '0'

    # Pesos para CNPJ
    pesos = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    
    # Validação dos dois últimos dígitos
    return cnpj[-2:] == (calcular_digito(cnpj, pesos) + calcular_digito(cnpj, pesos + [6]))

def remover_caracteres_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    return cpf

def remover_caracteres_cnpf(cnpj):
    cnpj = re.sub(r'\D', '', cnpj)
    return cnpj

def validar_AreaTotal(area_total_ha,area_agricola_ha,area_vegetacao_ha):
     soma_areas = area_vegetacao_ha + area_agricola_ha
     if  soma_areas <=  area_total_ha:
        return True
     else:
        return False
     
#Calcula o total de propriedades
def total_propriedades(produtores):   
     total = len(produtores)
     return total   
     
# Calcula o total de hectares usando list comprehension
def total_hectares(produtores):
    return sum(int(produtor.area_total_ha) for produtor in produtores if produtor.area_total_ha is not None)