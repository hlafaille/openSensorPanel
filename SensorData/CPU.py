import psutil
from pyspectator.processor import Cpu
from time import sleep


def temp():
    temp = list(psutil.sensors_temperatures().items())
    return str(round(temp[1][1][1][1]))


def frequency():
    return str(int(psutil.cpu_freq()[0])/1000)


def load():
    cpu = Cpu(monitoring_latency=1)
    return str(cpu.load)


def name():
    cpu = Cpu(monitoring_latency=1)
    return cpu.name
