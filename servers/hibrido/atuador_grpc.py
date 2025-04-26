import grpc
from concurrent import futures
import atuador_pb2
import atuador_pb2_grpc

class AtuadorService(atuador_pb2_grpc.AtuadorServiceServicer):
    def ExecutarComando(self, request, context):
        comando = request.nome
        print(f"[ATUADOR gRPC] Comando recebido: {comando}")

        if comando == "ligar luz":
            acao = "💡 Luz ligada."
        elif comando == "desligar ar":
            acao = "❄️ Ar condicionado desligado."
        elif comando == "abrir porta":
            acao = "🚪 Porta aberta."
        else:
            acao = "⚠️ Comando desconhecido."

        print(f"[ATUADOR gRPC] {acao}")
        return atuador_pb2.Resposta(status=acao)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    atuador_pb2_grpc.add_AtuadorServiceServicer_to_server(AtuadorService(), server)
    server.add_insecure_port('[::]:8000')
    server.start()
    print("[ATUADOR gRPC] Servidor iniciado na porta 8000...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
