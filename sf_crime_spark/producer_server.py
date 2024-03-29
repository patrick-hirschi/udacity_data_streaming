from kafka import KafkaProducer
import json
import time


class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    def generate_data(self):
        print(self.topic)
        with open(self.input_file, 'r') as f:
            data = json.load(f)
            
            for line in data:
                message = self.dict_to_binary(line)
            
                print(message)
                self.send(self.topic, message)
                time.sleep(1)

    def dict_to_binary(self, json_dict):
        data = json.dumps(json_dict)
        return data.encode('utf-8')