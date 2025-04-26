from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def publicar_dado_sensor(mensagem: str):
    try:
        tipo, valor = mensagem.split(":")
        payload = {"tipo": tipo, "valor": float(valor)}
        producer.send("sensor.dados", payload)
        print(f"[MIDDLEWARE SENSOR] Publicado no Kafka: {payload}")
    except Exception as e:
        print(f"[MIDDLEWARE SENSOR] Erro: {e}")
