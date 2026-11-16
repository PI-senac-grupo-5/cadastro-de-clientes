from dataclasses import dataclass


@dataclass
class Cliente:
    nome_completo: str
    email: str
    data_nasc: str
    telefone: str
    cep: str
    cpf: str = ""
    cnpj: str = ""


def __post_init__(self):
    if self.cpf == "" and self.cnpj == "":
        print("campos 'cnpj' ou 'cpf' não preenchidos")
        raise ValueError("Erro na validação do cliente")
