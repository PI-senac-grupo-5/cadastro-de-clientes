from typing import List

from database import mongodb
from entities.cliente import Cliente


def __mockar_cliente():
    # dados mock enquanto não temos chamadas ao banco de dados
    return [
        Cliente(
            nome_completo="Guilherme Matte",
            email="guilherme@email.com",
            data_nasc="2004-05-15",
            telefone="51999999999",
            cep="90010-150",
            cpf="12345678900"
        ),
        Cliente(
            nome_completo="Lucas Randon",
            email="lucas@email.com",
            data_nasc="2003-08-22",
            telefone="51988888888",
            cep="90020-100",
            cpf="98765432100"
        ),
        Cliente(
            nome_completo="Anne Caroline",
            email="anne@email.com",
            data_nasc="2002-11-10",
            telefone="51977777777",
            cep="90030-200",
            cnpj="12345678000199"
        ),
        Cliente(
            nome_completo="Guilherme Silva",
            email="guilherme.silva@email.com",
            data_nasc="1998-03-12",
            telefone="51999912345",
            cep="90040-300",
            cpf="11122233344"
        ),
        Cliente(
            nome_completo="Maria Eduarda",
            email="maria@email.com",
            data_nasc="2000-07-25",
            telefone="51988812345",
            cep="90050-400",
            cpf="22233344455"
        ),
        Cliente(
            nome_completo="Lucas Gabriel",
            email="lucas.gabriel@email.com",
            data_nasc="1999-12-05",
            telefone="51999945678",
            cep="90060-500",
            cpf="33344455566"
        ),
        Cliente(
            nome_completo="Ana Carolina",
            email="ana@email.com",
            data_nasc="2001-09-18",
            telefone="51977712345",
            cep="90070-600",
            cpf="44455566677"
        ),
        Cliente(
            nome_completo="Guilherme Oliveira",
            email="oliveira@email.com",
            data_nasc="1997-02-28",
            telefone="51988845678",
            cep="90080-700",
            cpf="55566677788"
        )
    ]


def filtrar_clientes(filter):
    """
    Filtra os clientes com base no telefone e/ou nome completo.

    Os filtros são aplicados em conjunto quando ambos são informados (AND).
    A busca por telefone e nome aceita correspondências parciais.
    A comparação de nomes ignora diferenças entre maiúsculas e minúsculas.

    Caso nenhum filtro seja informado, retorna todos os clientes cadastrados.

    :param filter: Trecho do telefone ou nome completo utilizado para filtrar os clientes (opcional).
    :return: Lista de clientes que correspondem aos filtros ou todos os clientes caso nenhum filtro seja informado.
    """

    clientes: List[Cliente] = mongodb.find(filter_value=filter)
    if len(clientes) == 0:
        print(f"Nenhum cliente encontrado para o filtro informado: {filter}")
    return clientes


def cadastrar_cliente(cliente: Cliente):
    mongodb.save(cliente)
    return cliente.id


def atualizar_cliente(cliente: Cliente):
    id = cliente.id

    if not id:
        raise ValueError("Id do cliente não informado")
    mongodb.update(id, cliente)
    return id


def deletar_cliente(cliente_id):
    if not cliente_id:
        raise ValueError("Id do cliente não informado")
    mongodb.delete(cliente_id)
