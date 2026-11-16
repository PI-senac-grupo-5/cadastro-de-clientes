# Como usar — Inicialização do MongoDB

Este guia explica como executar o script responsável por preparar o banco de dados do sistema de Cadastro de Clientes.

## 1. O que o script faz?

O arquivo `init-mongo.js` automatiza a preparação do banco de dados MongoDB.

Quando executado, ele:

- Acessa o banco de dados `cadastro_clientes`.
- Verifica se a coleção `clientes` já existe.
- Cria a coleção caso ela ainda não exista.
- Informa no terminal se a coleção foi criada ou se já estava disponível.

**Importante:** o script não apaga os dados existentes e pode ser executado novamente sem recriar a coleção.

## 2. Pré-requisitos

Antes de executar, é necessário ter:

- MongoDB Community Server instalado.
- Serviço do MongoDB em execução.
- MongoDB Shell (`mongosh`) instalado.
- Terminal aberto na pasta raiz do projeto.

## 3. Como executar

Abra o terminal na pasta principal do projeto e execute o comando:

```powershell
mongosh "mongodb://localhost:27017" --file scripts/init-mongo.js
```

### O que esse comando faz?

- `mongosh`: abre o terminal de comandos do MongoDB.
- `mongodb://localhost:27017`: conecta ao MongoDB instalado no próprio computador.
- `--file`: informa que será executado um arquivo de comandos.
- `scripts/init-mongo.js`: indica o caminho do script que será executado.

## 4. Resultado esperado

Se a coleção ainda não existir, o terminal exibirá:

```text
Coleção clientes criada!
Banco cadastro_clientes preparado!
```

Se a coleção já existir, exibirá:

```text
Coleção clientes já existe.
Banco cadastro_clientes preparado!
```

## 5. Como verificar no MongoDB Compass

1. Abra o MongoDB Compass.
2. Conecte-se utilizando:

```text
mongodb://localhost:27017
```

3. Localize o banco `cadastro_clientes`.
4. Abra a coleção `clientes`.

Se tudo estiver correto, a estrutura estará pronta para ser utilizada pelo backend do sistema.

## 6. Estrutura criada

```text
cadastro_clientes
└── clientes
```

