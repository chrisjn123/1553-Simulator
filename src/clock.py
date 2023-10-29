''' Clock module for 1553 Sim. '''
from numpy import pi, linspace
from scipy.signal import square
from itertools import cycle
from cpuinfo import get_cpu_info
from time import time

CPU_RATE =  get_cpu_info()['hz_actual'][0]

class Clock:
    def __init__(self, real_time: bool, rate: int) -> None:
        self.real = bool(real_time) if real_time else False
        self.rate = rate
        self.stopped = False
