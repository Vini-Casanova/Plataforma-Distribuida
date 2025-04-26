import socket
import grpc
import sensores_pb2
import sensores_pb2_grpc

UDP_IP = "0.0.0.0"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

# Conectando ao microsserviço gRPC
channel = grpc.insecure_channel('localhost:50051')
cliente = sensores_pb2_grpc.SensorServiceStub(channel)

while True:
    data, addr = sock.recvfrom(1024)
    leitura = data.decode()
    tipo, valor = leitura.split(':')
    print(f"[Gateway] Recebido de {addr}: {tipo} = {valor}")

    # Enviando para o microsserviço gRPC
    resposta = cliente.EnviarDado(
        sensores_pb2.DadoSensor(tipo=tipo, valor=float(valor))
    )
    print(f"[Gateway] gRPC resposta: {resposta.status}")
