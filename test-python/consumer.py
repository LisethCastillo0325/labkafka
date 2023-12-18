import json
from kafka import KafkaConsumer


# Configura los parámetros del consumidor
topics = ['univalle-ideas']
conf = {
    'bootstrap_servers': ['localhost:9092'],
    'group_id': 'test-group-python',
    'client_id': 'python-comsumer',
    'auto_offset_reset': 'earliest'
}

consumer = KafkaConsumer(*topics, **conf)

for message in consumer:
    value = json.loads(message.value.decode('utf-8'))
    print("\nTopic: ", message.topic)
    print("Partition: ", message.partition)
    print(value)