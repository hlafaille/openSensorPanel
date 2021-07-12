import psutil
import config


def total():
    return(str(round(psutil.virtual_memory()[0]/1024/1024/1024, 2)))

def available():
    return(str(round(psutil.virtual_memory()[1]/1024/1024/1024, 2)))
