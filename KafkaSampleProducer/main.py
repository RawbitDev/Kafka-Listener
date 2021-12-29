import os
import time
import random
import logging
from quoters import Quote
from kafka import KafkaProducer

KAFKA_URL = os.environ['KAFKA_URL']
KAFKA_TOPIC = os.environ['KAFKA_TOPIC']
connected = False

logging.basicConfig(format='[%(asctime)s] %(levelname)s %(message)s', level=logging.INFO)

while not connected:
    try:
        producer = KafkaProducer(bootstrap_servers=[KAFKA_URL])
        connected = True		
    except Exception:
        logging.warning('No kafka brokers available! Retrying in 3 seconds...')
        time.sleep(3)
		
while True:		
    msg = Quote.print_programming_quote().split("“")[1][:-1]
    producer.send(KAFKA_TOPIC, str.encode(msg))
    logging.info('Sent message "' + msg + '" to kafka topic "' + KAFKA_TOPIC + '"!')
    producer.flush()
    time.sleep(random.randint(25, 300) / 100)