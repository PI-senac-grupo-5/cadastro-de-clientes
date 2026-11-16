from entities.cliente import Cliente
from flask import Blueprint, jsonify, request

from services import clientes_service

router = Blueprint(
    "clientes",
    __name__,
    # todos nossos endpoints desse controller começaram com "/api/clientes"
    url_prefix="/api/clientes")


@router.get("")
def listar_todos_clientes():
    # body json da requisição
    filtros = request.get_json(silent=True) or {}

    telefone = filtros.get('telefone')
    nome_completo = filtros.get('nome_completo')

    clientes = clientes_service.filtrar_clientes(
        telefone=telefone,
        nome_completo=nome_completo
    )

    return jsonify({"clientes": clientes}), 200

@router.post("")
def cadastrar_cliente():
    # body json da requisição
    body = request.get_json(silent=True) or {}
    cliente = clientes_service.cadastrar_cliente(Cliente(**body))
    


    return jsonify({"cliente": cliente,"mensagem":"cliente cadastrado com sucesso"}), 201
