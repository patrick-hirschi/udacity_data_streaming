import producer_server

def run_kafka_server():
    producer = producer_server.ProducerServer(
        input_file='./police-department-calls-for-service.json',
        topic='com.udacity.dep.police.service',
        bootstrap_servers='localhost:9092',
        client_id='com.udacity.dep.police.broker'
    )

    return producer


def feed():
    producer = run_kafka_server()
    print("attempt start")
    producer.generate_data()


if __name__ == "__main__":
    feed()