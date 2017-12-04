"""task3 """
# Create a simple, separate python app which would monitor the your server.
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
    while True:
        timestamp = str(datetime.datetime.now()).split('.')[0]
        result = str(SNAPSHOT) + " " + str(counter) + ": " + timestamp \
                 + " "+" CPU Load: " + str(psutil.cpu_percent(0.5, 0)) + \
         " VM Usage: " + str(psutil.virtual_memory().used/1024**2) \
         + " SWAP Usage: " + str(psutil.swap_memory().used/1024**2) \
                 + " Disk I/O: read_bytes: " + str(DISK[2]) + \
         " write_bytes: " + str(DISK[3]) + " read time: " \
                 + str(DISK[4]) + " write time: " + str(DISK[5]) + \
         " Network: " + "bytes_sent(lo0): " \
         + str(NETWORK['lo0'][0])+" bytes_recv(lo0): " \
                 + str(NETWORK['lo0'][1]) + " bytes_sent(en0): " \
                 + str(NETWORK['en0'][0])\
         + " bytes_recv(en0): " + str(NETWORK['en0'][1])
        file = open(path+"."+output, 'a')
        file.write(result + "\n")
        file.close()
        counter += 1
        time.sleep(int(interval))


monitor_app(interval, output, counter, path)

