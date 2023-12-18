import json

from kafka import KafkaProducer


topics = ['univalle-ideas']
conf = {
    'bootstrap_servers': ['localhost:9092'],
    'client_id': 'python-producer',
    'value_serializer': lambda v: json.dumps(v).encode('utf-8')  # Serialize json messages
}
producer = KafkaProducer(**conf)

for x in range(5):
    mensaje = {
        'message': f'prueba mensaje {x}',
        'data': [1, 2, 3]
    }  
    producer.send(*topics, value=mensaje)


 # Cierra el productor
producer.close()