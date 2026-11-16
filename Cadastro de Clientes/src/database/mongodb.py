"""
Módulo de conexão e gerenciamento de clientes no MongoDB.

Este módulo estabelece a conexão com o banco de dados
'cadastro_clientes' e disponibiliza os métodos para
manipulação dos registros da collection 'clientes'.

Métodos disponíveis:

    save(cliente):
        Recebe um objeto Cliente e salva no banco de dados.

    delete(_id):
        Exclui um cliente utilizando seu identificador (_id).
        Não retorna valor.

    update(_id, cliente):
        Atualiza os dados de um cliente utilizando seu identificador.
        Não retorna valor.

    find_all():
        Busca todos os registros da collection e retorna
        uma lista de objetos Cliente.

    find_cliente(filtro):
        Busca clientes pelo nome completo ou telefone
        e retorna uma lista de objetos Cliente.

Observação:
    Durante as buscas, caso ocorra um ValueError ao instanciar
    um objeto Cliente, o registro será ignorado e a busca
    continuará com o próximo registro.
"""

from pymongo import MongoClient
from dataclasses import asdict
from bson import ObjectId
from src.entities.cliente import Cliente


# Conexão com MongoDB
client = MongoClient("mongodb://localhost:27017/")

database = client["cadastro_clientes"]

clientes = database["clientes"]

def save(cliente):
    dados = asdict(cliente)
    dados.pop("id", None)

    resultado = clientes.insert_one(dados)

    cliente.id = str(resultado.inserted_id)
    
def delete(_id):
    clientes.delete_one({
        "_id": ObjectId(_id)
    })
    
def update(_id, cliente):
    dados = asdict(cliente)
    dados.pop("id", None)

    clientes.update_one(
        {"_id": ObjectId(_id)},
        {"$set": dados}
    )

def find_all():
    lista_clientes = []
    
    for registro in clientes.find():
        try:
            registro["id"] = str(registro.pop("_id"))
            cliente = Cliente(**registro)
            lista_clientes.append(cliente)
        
        except ValueError:
            continue
    
    return lista_clientes

def find_cliente(filtro):
    lista_clientes = []
    
    registros = clientes.find({
        "$or": [
            {"nome_completo": {"$regex": filtro, "$options": "i"}},
            {"telefone": {"$regex": filtro, "$options": "i"}}
        ]
    })
    
    for registro in registros:
        try:
            registro["id"] = str(registro.pop("_id"))
            cliente = Cliente(**registro)
            lista_clientes.append(cliente)
        
        except ValueError:
            continue
    
    return lista_clientes