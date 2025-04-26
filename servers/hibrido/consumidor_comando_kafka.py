from kafka import KafkaConsumer
import grpc, json
import atuador_pb2
import atuador_pb2_grpc

consumer = KafkaConsumer(
    'comando.atuador',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

cliente = atuador_pb2_grpc.AtuadorServiceStub(grpc.insecure_channel('localhost:8000'))

for msg in consumer:
    comando = msg.value["comando"]
    resposta = cliente.ExecutarComando(atuador_pb2.Comando(nome=comando))
