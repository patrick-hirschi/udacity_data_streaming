import asyncio

from confluent_kafka import Consumer
from confluent_kafka.admin import AdminClient, NewTopic

async def consume(topic_name):
    consumer = Consumer({
        'bootstrap.servers': 'PLAINTEXT://localhost:9092', # Thanks to: https://github.com/weisurya/python-kafka-spark-sf-crime/blob/master/consumer_server.py
        'group.id': '0',
    })
    
    consumer.subscribe([topic_name])
    
    while True:
        messages = consumer.consume(10, timeout=1.0)
        
        for message in messages:
            if message is None:
                print('Message not found')
            elif message.error() is not None:
                print(f'Error: {message.error()}')
            else:
                print(f'{message.value()}\n')
                
        await asyncio.sleep(TIMEOUT)
                
def run_consumer():
    try:
        asyncio.run(consume('com.udacity.dep.police.service'))
        
    except KeyboardInterrupt as e:
        print("Shutting down...")
        
if __name__ == '__main__':
    run_consumer()