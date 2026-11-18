from dataclasses import dataclass
from typing import Optional


@dataclass
class Cliente:
    nome_completo: str
    email: str
    data_nasc: str
    telefone: str
    sexo: str
    cep: str
    cpf: str = ""
    cnpj: str = ""
    # id gerado pelo mongodb
    id: Optional[str] = None

    def __post_init__(self):
        if self.cpf == "" and self.cnpj == "":
            print("campos 'cnpj' ou 'cpf' não preenchidos")
            raise ValueError("Erro na validação do cliente")

    def to_dict(self):
        return self.__dict__
