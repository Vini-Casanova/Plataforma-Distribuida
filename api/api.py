from flask import Flask, request
from flask_cors import CORS
import socket

app = Flask(__name__)
CORS(app)  # ← habilita CORS para todas as rotas

GATEWAY_TCP_HOST = "127.0.0.1"
GATEWAY_TCP_PORT = 7000

@app.post("/enviar")
def enviar_comando():
    data = request.get_json()
    comando = data.get("comando", "")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((GATEWAY_TCP_HOST, GATEWAY_TCP_PORT))
            s.sendall(comando.encode())
        return {"status": "ok", "mensagem": f"Comando '{comando}' enviado com sucesso"}, 200
    except Exception as e:
        return {"status": "erro", "mensagem": str(e)}, 500

if __name__ == "__main__":
    app.run(port=8080)
