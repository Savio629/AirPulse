# kafka-producer/producer.py
import pandas as pd
from kafka import KafkaProducer
import json
import time

# Read the air quality dataset
data = pd.read_csv('/kafka-producer/air_quality_data.csv')

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

# Produce messages to Kafka
for index, row in data.iterrows():
    producer.send('air_quality', value=row.to_dict())
    print(f'Sent: {row.to_dict()}')
    time.sleep(0.1)  # Sleep to mimic real-time data streaming

producer.flush()
