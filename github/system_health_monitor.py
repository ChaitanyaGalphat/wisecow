import psutil
import shutil
import logging

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80.0
MEMORY_THRESHOLD = 80.0
DISK_THRESHOLD = 80.0

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {cpu_usage}%')
        print(f'Alert: High CPU usage detected: {cpu_usage}%')
    else:
        logging.info(f'CPU usage is normal: {cpu_usage}%')

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f'High memory usage detected: {memory_usage}%')
        print(f'Alert: High memory usage detected: {memory_usage}%')
    else:
        logging.info(f'Memory usage is normal: {memory_usage}%')

def check_disk_space():
    total, used, free = shutil.disk_usage("/")
    disk_usage = (used / total) * 100
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f'Low disk space detected: {disk_usage:.2f}% used')
        print(f'Alert: Low disk space detected: {disk_usage:.2f}% used')
    else:
        logging.info(f'Disk space usage is normal: {disk_usage:.2f}% used')

def check_running_processes():
    process_count = len(psutil.pids())
    logging.info(f'Number of running processes: {process_count}')

if __name__ == "__main__":
    check_cpu_usage()
    check_memory_usage()
    check_disk_space()
    check_running_processes()
    print("System health check complete. Check 'system_health.log' for details.")
