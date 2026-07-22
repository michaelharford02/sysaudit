import psutil


def get_memory_info():
    return psutil.virtual_memory()
