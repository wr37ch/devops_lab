import time
import datetime
import psutil
import configparser


config = configparser.RawConfigParser()
config.read('config.ini')
output = config.get('common', 'output')
interval = config.get('common', 'interval') #time is in seconds
counter = int(config.get('common', 'counter'))


class Monitor:
    def __init__(self):
        self.cpu = None
        self.vm = None
        self.swap = None
        self.disk = None
        self.network = None
        self.timestamp = None

    def data(self):
        self.cpu = 'CPU: ' + str(psutil.cpu_percent(0.5, 0))
        self.vm = " VM: " + str(psutil.virtual_memory().used / 1024 ** 2)
        self.swap = " Swap: " + str(psutil.swap_memory().used / 1024 ** 2)
        self.disk = " Disk I/O: read_bytes: " + str(psutil.disk_io_counters()[2]) + " write_bytes: " + str(
            psutil.disk_io_counters()[3]) + " read time: " + str(psutil.disk_io_counters()[4]) + \
                    " write time: " + str(psutil.disk_io_counters()[5])
        self.network = " Network: bytes_sent(lo0): " + str(psutil.net_io_counters(pernic=True)['lo'][0]) \
                       + " bytes_received(lo): " + str(psutil.net_io_counters(pernic=True)['lo'][1])
        self.timestamp = str(datetime.datetime.now()).split('.')[0]


class LogWriter(Monitor):

    def __init__(self):
        super().__init__()

    def write(self, logfile='output'+output):
        Monitor.data(self)
        global counter
        counter += 1
        file = open(logfile, 'a')
        file.write('SNAPSHOT {0}: {1}'.format(counter, self.timestamp))
        file.write(" " + self.cpu)
        file.write(" " + self.vm)
        file.write(" " + self.swap)
        file.write(" " + self.disk)
        file.write(" " + self.timestamp + "\n ")
        file.write("\n")
        file.close()


a = LogWriter()

while True:
    a.write()
    time.sleep(int(interval))
