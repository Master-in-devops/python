import psutil

def get_disk_usage(path="/"):
    # Get disk usage statistics
    usage = psutil.disk_usage(path)
    
    # Convert bytes to Gigabytes for readability
    total_gb = usage.total / (1024**3)
    used_gb = usage.used / (1024**3)
    free_gb = usage.free / (1024**3)
    percent = usage.percent

    print(f"Disk Usage for '{path}':")
    print(f"Total:   {total_gb:.2f} GB")
    print(f"Used:    {used_gb:.2f} GB")
    print(f"Free:    {free_gb:.2f} GB")
    print(f"Percent: {percent}%")

if __name__ == "__main__":
    # Use 'C:\\' for Windows or '/' for Linux/macOS
    get_disk_usage("/")