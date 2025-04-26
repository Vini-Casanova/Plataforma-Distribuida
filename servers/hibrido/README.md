# 📡 Plataforma Distribuída de Monitoramento e Controle – SmartCampus Solutions

Este projeto simula uma **plataforma distribuída de monitoramento e controle de ambientes inteligentes** em um campus universitário, utilizando comunicação via **sockets (UDP/TCP)**, **Kafka como middleware de mensageria**, e **gRPC para integração com microsserviços e atuadores**.

## Equipe
Vinicius Casanova
Lucas Alves
Ethan Maxelll
Raissa Souza

---

## 🔧 Tecnologias Utilizadas

- Python 3.11+
- gRPC (Protocol Buffers)
- Apache Kafka + Zookeeper
- Kafka-Python
- Sockets (UDP/TCP)
- Arquitetura orientada a microsserviços
- Log de auditoria via arquivo `.log`

---

## 📐 Arquitetura do Sistema

```plaintext
[SENSOR UDP]       → [GATEWAY HÍBRIDO] → Middleware Sensor → Kafka (sensor.dados) → CONSUMIDOR → gRPC → Microsserviço

[COMANDO TCP]      → [GATEWAY HÍBRIDO] → Middleware Comando → Kafka (comando.atuador) → CONSUMIDOR → gRPC → Atuador

---

## ▶️ Execução Local

1. Instale dependências

pip install -r requirements.txt

2. Compile os arquivos .proto

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. sensores.proto
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. atuador.proto

3. Inicie o Kafka e Zookeeper

    Se tiver Docker:

docker compose up -d

🧪 Execução dos Componentes
Em terminais separados, execute:

# Microsserviço gRPC
python microsservico_grpc.py

# Atuador gRPC
python atuador_grpc.py

# Consumidores Kafka
python consumidor_sensor_kafka.py
python consumidor_comando_kafka.py

# Gateway híbrido
python gateway_hibrido.py

# Enviar comandos e sensores (em paralelo)
python sensor_temperatura_udp.py
python comando_tcp.py

📊 Logs de Auditoria

    📄 sensor_auditoria.log → Registra dados recebidos dos sensores

    📄 comando_auditoria.log → Registra comandos executados