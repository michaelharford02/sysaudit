import subprocess


def get_selinux_status():
    try:
        selinux_status = subprocess.run(
            ["getenforce"],
            capture_output=True,
            text=True
        )
        return selinux_status.stdout.strip()
    except FileNotFoundError:
        return None

def get_firewalld_status():
    try:
        firewalld_status = subprocess.run(
            ["systemctl", "is-active", "firewalld"],
            capture_output=True
        )
        if firewalld_status.returncode == 0:
            return "Active"
        elif firewalld_status.returncode == 3:
            return "Inactive"
        else:
            return None
    except FileNotFoundError:
        return None
