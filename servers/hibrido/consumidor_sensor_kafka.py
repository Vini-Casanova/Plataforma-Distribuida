from kafka import KafkaConsumer
import grpc, json
import sensores_pb2
import sensores_pb2_grpc

consumer = KafkaConsumer(
    'sensor.dados',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

cliente = sensores_pb2_grpc.SensorServiceStub(grpc.insecure_channel('localhost:50051'))

for msg in consumer:
    dado = msg.value
    resposta = cliente.EnviarDado(sensores_pb2.DadoSensor(
        tipo=dado["tipo"],
        valor=dado["valor"]
    ))