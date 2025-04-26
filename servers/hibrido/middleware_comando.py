from kafka import KafkaProducer
import json


producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def publicar_comando(comando: str):
    try:
        payload = {"comando": comando}
        producer.send("comando.atuador", payload)
        print(f"[MIDDLEWARE COMANDO] Publicado no Kafka: {payload}")
    except Exception as e:
        print(f"[MIDDLEWARE COMANDO] Erro: {e}")
