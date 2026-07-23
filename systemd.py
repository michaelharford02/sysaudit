import subprocess


def get_failed_units() -> list[str]:
    failed_units = subprocess.run(
        ["systemctl", "--failed", "--no-legend", "--plain"],
        capture_output=True,
        text=True,
    )
    units = failed_units.stdout.splitlines()
    unit_names = []
    for unit in units:
        stdout_list = unit.split()
        unit_names.append(stdout_list[0])
    return unit_names
