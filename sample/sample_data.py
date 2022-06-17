import random


class MeasurementValue:

    def __init__(self):
        self.temperature = round(random.uniform(20, 38), 2)
        self.rssi = random.randint(0, 46)
        self.humidity = round(random.uniform(0, 101), 2)

    def generate_json(self):
        json = {
            'temperature': self.temperature,
            'rssi': self.rssi,
            'humidity': self.humidity
        }
        return json


if __name__ == "__main__":
    obj = MeasurementValue()
    print(obj.generate_json())
