import psutil
def temp():
    temp = list(psutil.sensors_temperatures().items())
    #print(str(temp[2][1][0][1]))
    return str(temp[2][1][0][1])