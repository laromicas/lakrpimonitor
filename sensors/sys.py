from psutil import boot_time, sensors_temperatures, virtual_memory
import subprocess
import time
import os

class System():
    boot_time = 0
    ram = None
    def __init__(self):
        self.boot_time = boot_time()
    def uptime(self):
        return time.time() - self.boot_time
    def cpu_usage(self):
        load1, load5, load15 = os.getloadavg()
        cpu_usage = (load15/os.cpu_count()) * 100
        return cpu_usage
    def cpu_temperature(self):
        return sensors_temperatures()['cpu_thermal'][0].current
    def fan_speed(self):
        result = subprocess.run(['fan_speed'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        return float(result.strip())

    def ram_usage(self):
        total_memory, used_memory, free_memory = map(
            int, os.popen('free -t -m').readlines()[-1].split()[1:])
        return round((used_memory/total_memory) * 100, 2)
    def get_ram(self):
        self.ram = virtual_memory()
    def ram_total(self):
        self.get_ram()
        return self.ram.total
    def ram_free(self):
        self.get_ram()
        return self.ram.free
    def ram_available(self):
        self.get_ram()
        return self.ram.available
    def ram_used(self):
        self.get_ram()
        return self.ram.used
    def ram_percent(self):
        self.get_ram()
        return self.ram.percent


# sys = System()
# sys.fan_speed()