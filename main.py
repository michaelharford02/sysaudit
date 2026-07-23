import cpu
import disk
import memory
import system
import systemd


def main():
    days, hours, minutes, seconds = system.get_uptime()
    one, five, fifteen = cpu.get_cpu_load_avg()
    memory_info = memory.get_memory_info()
    failed_units = systemd.get_failed_units()
    disk_info = disk.get_fs_usage()
    print("System Audit Report")
    print("===================")
    print(f"Hostname: {system.get_hostname()}")
    print(f"OS: {system.get_os()}")
    print(f"Kernel: {system.get_kernel()}")
    print(f"Uptime: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
    print()
    print("CPU")
    print("---")
    print(f"Load Average: {one:.2f}, {five:.2f}, {fifteen:.2f}")
    print(f"CPU Count: {cpu.get_cpu_count()}")
    print()
    print("Memory")
    print("------")
    print(f"Used: {memory_info.used / (1024 ** 3):.1f} GiB / {memory_info.total / (1024 ** 3):.1f} GiB")
    print()
    print("Disk")
    print("----")
    for mount, usage in disk_info.items():
        print(f"{mount}: {usage.used / usage.total * 100:.1f}% used")
    print()
    print("Services")
    print("--------")
    print(f"Failed systemd units: {len(failed_units)}")
    for unit in failed_units:
        print(f"  {unit}")
    print()
    print("Security")
    print("--------")



if __name__ == "__main__":
    main()
