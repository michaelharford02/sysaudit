import psutil
import shutil


def get_fs_usage():
    mounted_drives =  psutil.disk_partitions()
    fs_usage = {}
    for fs in mounted_drives:
        mount = fs.mountpoint
        usage = shutil.disk_usage(mount)
        fs_usage[mount] = usage
    return fs_usage
