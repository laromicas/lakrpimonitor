class Screen():
    sensors = []


class SensorBuilder():
    sensor_type = 'text'
    def type(self, sensor_type):
        self.sensor_type = sensor_type
        return self