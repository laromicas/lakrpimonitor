from common.format import human_time_duration

class SensorCollect():

    def uptime(self, system):
        return human_time_duration(system.uptime())

    def cpu_temperature(self, system):
        return '%.2f°C' % system.cpu_temperature()

    def fan_speed(self, system):
        return '%s RPM' % system.fan_speed()
