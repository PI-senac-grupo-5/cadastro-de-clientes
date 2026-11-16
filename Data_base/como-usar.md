# Como usar — Inicialização do MongoDB

Este guia explica como executar o script responsável por preparar o banco de dados do sistema de Cadastro de Clientes.

## 1. O que o script faz?

O arquivo `init-mongo.js` automatiza a preparação do banco de dados MongoDB.

Quando executado, ele:

- Acessa o banco de dados `cadastro_clientes`.
- Verifica se a coleção `clientes` já existe.
- Cria a coleção caso ela ainda não exista.
- Informa no terminal se a coleção foi criada ou se já estava disponível.

**Importante:** o script não apaga os dados existentes e pode ser executado novamente sem tentar recriar a coleção.

## 2. Pré-requisitos

Antes de executar, é necessário ter:

- MongoDB Community Server instalado.
- Serviço do MongoDB em execução.
- MongoDB Shell (`mongosh`) instalado.
- Terminal aberto na pasta raiz do projeto.

## 3. Como executar

Abra o terminal na pasta principal do projeto e execute o comando:

```powershell
mongosh "mongodb://localhost:27017" --file Data_base/init-mongo.js
```

### O que esse comando faz?

- `mongosh`: abre o terminal de comandos do MongoDB.
- `mongodb://localhost:27017`: conecta ao MongoDB instalado no próprio computador.
- `--file`: informa que será executado um arquivo de comandos.
- `Data_base/init-mongo.js`: indica o caminho do script que será executado.

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

## 5. Ferramentas compatíveis

O projeto utiliza o MongoDB, portanto não é obrigatório utilizar exclusivamente o MongoDB Compass.

É possível utilizar diferentes ferramentas para visualizar e administrar o banco de dados, como:

- **MongoDB Compass:** interface gráfica oficial do MongoDB.
- **NoSQLBooster:** ferramenta para executar comandos e administrar bancos MongoDB.
- **DBeaver:** gerenciador de bancos de dados que oferece suporte ao MongoDB em versões e configurações compatíveis.

**Observação:** essas ferramentas são utilizadas para acessar e administrar o banco. O script `init-mongo.js` é executado pelo MongoDB Shell (`mongosh`), independentemente da ferramenta gráfica escolhida.

## 6. Como verificar no MongoDB Compass

Caso utilize o MongoDB Compass:

1. Abra o MongoDB Compass.
2. Conecte-se utilizando:

```text
mongodb://localhost:27017
```

3. Localize o banco `cadastro_clientes`.
4. Abra a coleção `clientes`.

Se tudo estiver correto, a estrutura estará pronta para ser utilizada pelo backend do sistema.

## 7. Estrutura criada

```text
cadastro_clientes
└── clientes
```

## 8. Observações finais

- O script prepara a estrutura inicial do banco de dados.
- Ele não cadastra clientes automaticamente.
- Ele não apaga documentos existentes.
- Pode ser executado novamente sem tentar criar uma coleção que já existe.
- O banco é criado localmente no computador