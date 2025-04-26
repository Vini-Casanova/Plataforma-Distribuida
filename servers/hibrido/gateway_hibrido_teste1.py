import socket
import threading
import grpc

# Importações do microsserviço (dados dos sensores)
import sensores_pb2
import sensores_pb2_grpc

# Importações do atuador (ações de controle)
import atuador_pb2
import atuador_pb2_grpc

# Configurações
UDP_PORT = 6000
TCP_PORT = 7000
GRPC_MICRO_HOST = "localhost:50051"
GRPC_ATUADOR_HOST = "localhost:8000"


def escutar_sensores_udp():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("0.0.0.0", UDP_PORT))
    print(f"[GATEWAY UDP] Escutando sensores na porta {UDP_PORT}...")

    canal_micro = grpc.insecure_channel(GRPC_MICRO_HOST)
    cliente_micro = sensores_pb2_grpc.SensorServiceStub(canal_micro)

    while True:
        data, addr = udp_socket.recvfrom(1024)
        mensagem = data.decode()
        print(f"[GATEWAY UDP] Recebido de {addr}: {mensagem}")

        try:
            tipo, valor = mensagem.split(":")
            valor = float(valor)
            resposta = cliente_micro.EnviarDado(sensores_pb2.DadoSensor(tipo=tipo, valor=valor))
            print(f"[GATEWAY → MICRO gRPC] Resposta: {resposta.status}")
        except Exception as e:
            print(f"[GATEWAY UDP] Erro: {e}")

def escutar_comandos_tcp():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind(("0.0.0.0", TCP_PORT))
    tcp_socket.listen()
    print(f"[GATEWAY TCP] Escutando comandos na porta {TCP_PORT}...")

    while True:
        conn, addr = tcp_socket.accept()
        with conn:
            print(f"[GATEWAY TCP] Conectado com {addr}")
            comando = conn.recv(1024).decode()
            if comando:
                print(f"[GATEWAY TCP] Comando recebido: {comando}")
                encaminhar_para_atuador_grpc(comando)

def encaminhar_para_atuador_grpc(comando):
    try:
        canal_atuador = grpc.insecure_channel(GRPC_ATUADOR_HOST)
        cliente_atuador = atuador_pb2_grpc.AtuadorServiceStub(canal_atuador)
        resposta = cliente_atuador.ExecutarComando(atuador_pb2.Comando(nome=comando))
        print(f"[GATEWAY → ATUADOR gRPC] Resposta: {resposta.status}")
    except Exception as e:
        print(f"[GATEWAY gRPC] Erro ao encaminhar para atuador: {e}")


if __name__ == "__main__":
    thread_udp = threading.Thread(target=escutar_sensores_udp)
    thread_tcp = threading.Thread(target=escutar_comandos_tcp)

    thread_udp.start()
    thread_tcp.start()

    thread_udp.join()
    thread_tcp.join()
