import psutil
import logging

# Set logging configuration
logging.basicConfig(filename='system_health.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define thresholds
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage

# CPU USAGE:
def check_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > CPU_THRESHOLD:
        message = f"ALERT: CPU usage is {cpu_percent}%, exceeding the threshold of {CPU_THRESHOLD}%."
        print(message)
        logging.warning(message)

# Memory usage:
def check_memory_usage():
    mem = psutil.virtual_memory()
    mem_percent = mem.percent
    if mem_percent > MEMORY_THRESHOLD:
        message = f"ALERT: Memory usage is {mem_percent}%, exceeding the threshold of {MEMORY_THRESHOLD}%."
        print(message)
        logging.warning(message)

# Disk space usges:
def check_disk_usage():
    disk_usage = psutil.disk_usage('/')
    disk_percent = disk_usage.percent
    if disk_percent > DISK_THRESHOLD:
        message = f"ALERT: Disk usage is {disk_percent}%, exceeding the threshold of {DISK_THRESHOLD}%."
        print(message)
        logging.warning(message)

# Running processes :
def check_running_processes():
    num_processes = len(psutil.pids())
    message = f"Number of running processes: {num_processes}"
    print(message)
    logging.info(message)

# Main function to run all checks above cases 
def main():
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()

if __name__ == "__main__":
    main()