# Para subir o servidor, esteja com o venv pronto dentro do diretorio "Cadastro de Clientes" e rode "python src/app.py"

from flask import Flask
from flask_cors import CORS

from controllers.cliente_controller import router as clientes_router

app = Flask(__name__)
app.register_blueprint(clientes_router)
CORS(app)


@app.route("/")
def home():
    return {"message": "API funcionando!"}


if __name__ == "__main__":
    app.run(debug=True)
