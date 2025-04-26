import grpc
from concurrent import futures
import sensores_pb2
import sensores_pb2_grpc

class SensorServiceServicer(sensores_pb2_grpc.SensorServiceServicer):
    def EnviarDado(self, request, context):
        print(f"[Microsserviço] Recebido: {request.tipo} = {request.valor}")
        # Aqui você pode gravar no banco, mandar pro Kafka etc.
        return sensores_pb2.Resposta(status="Recebido com sucesso")

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
sensores_pb2_grpc.add_SensorServiceServicer_to_server(SensorServiceServicer(), server)
server.add_insecure_port('[::]:50051')
server.start()
print("[Microsserviço] gRPC rodando na porta 50051")
server.wait_for_termination()
