from typing import Optional
from common.format import human_time_duration
from common.format import human_read_bytes
from pydantic import BaseModel


class Seconds(BaseModel):
    value: int
    def __init__(self, value):
        self.value = int(value)
    def str(self):
        return human_time_duration(self.value, 2)

class Percentage(BaseModel):
    total: float
    value: float
    threshold: Optional[float] = None
    def __init__(self, value, total):
        self.value = float(value)
        self.total = float(total)
    def str(self):
        return '%.1f%'%(self.value*100/self.total)

class Temperature(BaseModel):
    value: float
    threshold: Optional[float] = None
    monitor: str = '>'
    def __init__(self, value):
        self.value = int(value)
    def str(self):
        return '%.1f°C' % self.value()

class Speed(BaseModel):
    value: float
    threshold: Optional[float] = 0.1
    monitor: str = '<'
    def __init__(self, value):
        self.value = int(value)
    def str(self):
        return '%.1f RPM' % self.value()

class Memory(BaseModel):
    value: int
    threshold: Optional[int]
    monitor: str = '<'
    def __init__(self, value):
        self.value = int(value)
    def str(self):
        return human_read_bytes(self.value())
