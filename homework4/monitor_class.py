import time
import datetime
import psutil
import configparser


config = configparser.RawConfigParser()
config.read('config.ini')
output = config.get('common', 'output')
interval = config.get('common', 'interval') # time is in seconds
counter = int(config.get('common', 'counter'))


def get_time():
    return str(datetime.datetime.now()).split('.')[0]


class Monitor:
    def __init__(self):
        self.counter = counter
        self.cpu_load = psutil.cpu_percent(0.5, 0)
        self.vm_usage = psutil.virtual_memory().used / 1024 ** 2
        self.swap_usage = psutil.swap_memory().used / 1024 ** 2
        self.disk_rb = psutil.disk_io_counters()[2]
        self.disk_wb = psutil.disk_io_counters()[3]
        self.disk_rt = psutil.disk_io_counters()[4]
        self.disk_wt = psutil.disk_io_counters()[5]
        self.network_bs = psutil.net_io_counters(pernic=True)['lo0'][0]
        self.network_br = psutil.net_io_counters(pernic=True)['lo0'][1]

    def write(self):
        result = (
            'SNAPSHOT                   : {0}\n'
            'Date                       : {1}\n'
            'CPU load                   : {2}%\n'
            'VM usage                   : {3}mb\n'
            'SWAP usage                 : {4}mb\n'
            'Disk I/O: read_bytes       : {5} bytes\n'
            'Disk I/O: write_bytes      : {6} bytes\n'
            'Disk I/O: read time        : {7} \n'
            'Disk I/O: write time       : {8} \n'
            'Network bytes_sent(lo0)    : {9} bytes \n'
            'Network bytes_received(lo0): {10} bytes \n'.format(self.counter, timestamp, self.cpu_load,
                                                                self.vm_usage, self.swap_usage,
                                                                self.disk_rb, self.disk_wb, self.disk_rt,
                                                                self.disk_wt, self.network_bs, self.network_br))
        file = open('log' + output, 'a')
        file.write(result + "\n")
        file.close()


while True:
    writer = Monitor()
    timestamp = get_time()
    writer.write()
    counter += 1
    time.sleep(int(interval))

