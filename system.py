import os
import socket
from typing import Optional


def get_hostname() -> str:
    return socket.gethostname()


def get_os():
    with open("/etc/os-release") as file:
        name: Optional[str] = None
        version: Optional[str] = None

        for line in file:
            if line.startswith("NAME="):
                name = line.split("=", 1)[1].strip().strip('"')
            elif line.startswith("VERSION="):
                version = line.split("=", 1)[1].strip().strip('"')
    return f"{name} {version}"


def get_kernel():
    return os.uname().release


def get_uptime():
    with open("/proc/uptime") as file:
        contents = file.read()
        uptime = float(contents.split()[0])
        days = int(uptime // 86400)
        hours = int((uptime % 86400) // 3600)
        minutes = int((uptime % 3600) // 60)
        seconds = int(uptime % 60)
    return (days, hours, minutes, seconds)
