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

from bson import ObjectId
from pymongo import MongoClient

from src.entities.cliente import Cliente

# Conexão com MongoDB
client = MongoClient("mongodb://localhost:27017/")

database = client["cadastro_clientes"]

db = database["clientes"]


def save(customer: Cliente):
    data = customer.to_dict()
    data.pop("id", None)

    result = db.insert_one(data)

    customer.id = str(result.inserted_id)


def delete(_id):
    db.delete_one({
        "_id": ObjectId(_id)
    })


def update(_id, customer: Cliente):
    data = customer.to_dict()
    data.pop("id", None)

    db.update_one(
        {"_id": ObjectId(_id)},
        {"$set": data}
    )


def find(filter_value: str = None):
    customers = []

    if filter_value:
        filter = {
            "$or": [
                {"nome_completo": {"$regex": filter_value, "$options": "i"}},
                {"telefone": {"$regex": filter_value, "$options": "i"}}
            ]
        }
    else:
        filter = {}

    docs = db.find(filter)

    for doc in docs:
        try:
            doc["id"] = str(doc.pop("_id"))
            customer = Cliente(**doc)
            customers.append(customer)

        except ValueError:
            continue

    return customers
