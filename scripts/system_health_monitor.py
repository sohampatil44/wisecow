
import psutil
import logging
from datetime import datetime


logging.basicConfig(
    filename='system_health.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

CPU_THRESHOLD =80
MEMORY_THRESHOLD = 80  
DISK_THRESHOLD = 80

def check_cpu():
    usage = psutil.cpu_percent(interval=1)
    if usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {usage}%")
    return usage

def check_memory():
    mem = psutil.virtual_memory()
    usage = mem.percent
    if usage > MEMORY_THRESHOLD:
        logging.warning(f"High Memory usage detected: {usage}%")
    return usage

def check_disk():
    disk = psutil.disk_usage('/')
    usage = disk.percent
    if usage > DISK_THRESHOLD:
        logging.warning(f"High Disk usage detected: {usage}%")
    return usage

def main():
    logging.info("System health check started")
    cpu = check_cpu()
    mem = check_memory()
    disk = check_disk()
    logging.info(f"CPU: {cpu}%, Memory: {mem}%, Disk: {disk}%")
    print(f"CPU: {cpu}%, Memory: {mem}%, Disk: {disk}%")

if __name__ == "__main__":
    main()