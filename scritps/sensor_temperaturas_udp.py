import socket
import time
import random

GATEWAY_IP = '127.0.0.1'
GATEWAY_PORT = 6000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    temperatura = round(random.uniform(20.0, 30.0), 2)
    mensagem = f"temperatura:{temperatura}"
    sock.sendto(mensagem.encode(), (GATEWAY_IP, GATEWAY_PORT))
    print(f"[Sensor] Enviou: {mensagem}")
    time.sleep(5)
