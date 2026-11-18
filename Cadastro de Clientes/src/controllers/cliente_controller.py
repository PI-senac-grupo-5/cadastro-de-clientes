from flask import Blueprint, jsonify, request

from entities.cliente import Cliente
from services import clientes_service

router = Blueprint(
    "clientes",
    __name__,
    # todos os nossos endpoints desse controller começaram com "/api/clientes"
    url_prefix="/api/clientes")


@router.get("")
def listar_todos_clientes():
    # Obtém o filtro através da query string
    filtro = request.args.get("filtro")

    clientes = clientes_service.filtrar_clientes(
        filter=filtro
    )

    return jsonify({"clientes": clientes}), 200


@router.post("")
def cadastrar_cliente():
    # body json da requisição
    body = request.get_json(silent=True) or {}

    try:
        cliente_id = clientes_service.cadastrar_cliente(Cliente(**body))
        mensagem = "Cliente cadastrado com sucesso"
        status = 201
    except Exception as e:
        print(f"Falha ao cadastrar cliente: {e}")
        cliente_id = "ERROR"
        mensagem = "Falha ao cadastrar cliente"
        status = 500
    return jsonify({"cliente_id": cliente_id, "mensagem": mensagem}), status


@router.put("")
def atualizar_cliente():
    body = request.get_json(silent=True) or {}
    try:
        cliente_id = clientes_service.atualizar_cliente(Cliente(**body))
        mensagem = "Cliente cadastrado com sucesso"
        status = 200
    except Exception as e:

        print(f"Falha ao atualizar cliente: {e}")
        cliente_id = "ERROR"
        mensagem = "Falha ao atualizar cliente"
        status = 500
    return jsonify({"cliente_id": cliente_id, "mensagem": mensagem}), status


@router.delete("/<cliente_id>")
def deletar_cliente(cliente_id):
    try:
        clientes_service.deletar_cliente(cliente_id)
        return "", 204
    except Exception as e:
        print(f"Falha ao deletar cliente: {e}")
        return jsonify({"mensagem": "Falha ao deletar cliente"}), 500
