import os
import time
import logging
from kafka import KafkaConsumer

KAFKA_URL = os.environ['KAFKA_URL']
KAFKA_TOPIC = os.environ['KAFKA_TOPIC']
connected = False

logging.basicConfig(format='[%(asctime)s] %(levelname)s %(message)s', level=logging.INFO)

while not connected:
    try:
        consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=[KAFKA_URL])
        connected = True		
    except Exception:
        logging.warning('No kafka brokers available! Retrying in 3 seconds...')
        time.sleep(3)

for msg in consumer:
    logging.info('Received message "' + msg.value.decode("utf-8") + '" through kafka topic "' + KAFKA_TOPIC + '"!')
