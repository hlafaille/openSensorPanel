import math
import time
from threading import Thread
import speedtest
import config

class NetTest(Thread):
    def __init__(self):
        Thread.__init__(self)
        Thread.start(self)
        self.res_temp = ""

    def run(self):
        while True:
            st = speedtest.Speedtest()
            st.get_servers()
            st.get_best_server()
            st.download()
            st.upload()
            res = st.results.dict()
            self.res_temp = list(res.items())
            time.sleep(config.NETWORK['SPEEDTEST_REFRESH'])

    def ping(self):
        if not self.res_temp:
            return str("...")
        if self.res_temp:
            return str(round(self.res_temp[2][1]))

    def download(self):
        if not self.res_temp:
            return str("...")
        if self.res_temp:
            tempdl = math.trunc(self.res_temp[0][1])/1024/1024
            return str(round(tempdl))

    def upload(self):
        if not self.res_temp:
            return str("...")
        if self.res_temp:
            tempul = math.trunc(self.res_temp[1][1])/1024/1024
            return str(round(tempul))
