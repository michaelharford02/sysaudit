import os
from typing import Optional


def get_cpu_load_avg() -> tuple[float, float, float]:
    return os.getloadavg()


def get_cpu_count() -> Optional[int]:
    return os.cpu_count()
