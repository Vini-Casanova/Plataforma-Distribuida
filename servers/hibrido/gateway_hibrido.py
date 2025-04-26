import socket
import threading
from middleware_sensor import publicar_dado_sensor
from middleware_comando import publicar_comando

UDP_PORT = 6000
TCP_PORT = 7000

def escutar_udp():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", UDP_PORT))
    print(f"[UDP] Escutando sensores na porta {UDP_PORT}...")

    while True:
        data, addr = sock.recvfrom(1024)
        mensagem = data.decode()
        print(f"[UDP] Recebido: {mensagem}")
        publicar_dado_sensor(mensagem)


def escutar_tcp():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("0.0.0.0", TCP_PORT))
    sock.listen()
    print(f"[TCP] Escutando comandos na porta {TCP_PORT}...")

    while True:
        conn, addr = sock.accept()
        with conn:
            comando = conn.recv(1024).decode()
            print(f"[TCP] Comando recebido: {comando}")
            publicar_comando(comando)

if __name__ == "__main__":
    threading.Thread(target=escutar_udp).start()
    threading.Thread(target=escutar_tcp).start()
