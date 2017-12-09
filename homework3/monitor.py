"""task3 """
# Create a simple, separate python app which would monitor your server.
import time
import datetime
import psutil
import configparser
SNAPSHOT = "SNAPSHOT"
NETWORK = psutil.net_io_counters(pernic=True)
DISK = psutil.disk_io_counters()

config = configparser.RawConfigParser()
config.read('config.ini')
output = config.get('common', 'output')
interval = config.get('common', 'interval') # time is in seconds
counter = int(config.get('common', 'counter'))
path = config.get('common', 'path')


def monitor_app(interval, output, counter, path):
    """function which monitors CPU, memory, disks and network"""
    timestamp = str(datetime.datetime.now()).split('.')[0]
    cpu_load = psutil.cpu_percent(0.5, 0)
    vm_usage = psutil.virtual_memory().used/1024**2
    swap_usage = psutil.swap_memory().used/1024**2
    disk_rb = DISK[2]
    disk_wb = DISK[3]
    disk_rt = DISK[4]
    disk_wt = DISK[5]
    network_bs = NETWORK['lo0'][0]
    network_br = NETWORK['lo0'][1]
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
     'Network bytes_received(lo0): {10} bytes \n'.format(counter, timestamp,cpu_load, vm_usage, swap_usage, disk_rb, disk_wb, disk_rt,
                                                  disk_wt, network_bs, network_br))
    file = open(path+'.'+output, 'a')
    file.write(result + "\n")
    file.close()
    counter += 1


while True:
    monitor_app(interval, output, counter, path)
    time.sleep(int(interval))




