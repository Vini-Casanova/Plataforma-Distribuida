import socket

HOST = '127.0.0.1'
PORT = 7000

comando = input("Digite o comando (ligar luz / desligar ar / abrir porta): ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(comando.encode())
    print(f"[CLIENTE TCP] Comando enviado: {comando}")
