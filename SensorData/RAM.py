import psutil


def total():
    return(str(round(psutil.virtual_memory()[0]/1024/1024/1024, 2)))

def available():
    print(psutil.sensors_temperatures())
    return(str(round(psutil.virtual_memory()[1]/1024/1024/1024, 2)))
