import socket
import grpc
import atuador_pb2
import atuador_pb2_grpc

GATEWAY_PORT = 7000
GRPC_HOST = 'localhost:8000'

def encaminhar_para_atuador(comando):
    with grpc.insecure_channel(GRPC_HOST) as channel:
        stub = atuador_pb2_grpc.AtuadorServiceStub(channel)
        resposta = stub.ExecutarComando(atuador_pb2.Comando(nome=comando))
        print(f"[GATEWAY TCP→gRPC] Resposta do Atuador: {resposta.status}")

def iniciar_gateway_tcp():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('0.0.0.0', GATEWAY_PORT))
    servidor.listen()

    print(f"[GATEWAY TCP] Aguardando conexões na porta {GATEWAY_PORT}...")

    while True:
        conn, addr = servidor.accept()
        with conn:
            print(f"[GATEWAY TCP] Conectado com {addr}")
            comando = conn.recv(1024).decode()
            if comando:
                print(f"[GATEWAY TCP] Comando recebido: {comando}")
                encaminhar_para_atuador(comando)

if __name__ == "__main__":
    iniciar_gateway_tcp()
