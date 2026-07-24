sysaudit

sysaudit is a simple command-line tool that collects information about a Linux system and displays it in a formatted system audit report.

This project was created as a learning project to practice Python, working with Linux system information, third-party packages, subprocesses, and organizing a program into multiple modules.

Features

sysaudit currently reports:

Hostname
Operating system and version
Kernel version
System uptime
CPU load averages
CPU count
Memory usage
Disk usage for mounted filesystems
Failed systemd units
SELinux status
Firewalld status

Security checks that are unavailable on the system are reported as Not available.

Requirements
Linux
Python 3.9+
uv

Some checks depend on software available on the host system:

systemd is required for failed unit and firewalld checks.
SELinux tools are required to report SELinux status.
firewalld is required to report firewalld status.
Installation

Clone the repository:

git clone <repository-url>
cd sysaudit

Install the project's dependencies:

uv sync

uv sync creates the project's virtual environment and installs the dependencies specified in pyproject.toml.

Usage

Run the program with:

uv run python main.py

Example output:

System Audit Report
===================
Hostname: fedora
OS: Fedora Linux 44 (Workstation Edition)
Kernel: 7.1.4-200.fc44.x86_64
Uptime: 2 d, 1 h, 23 m, 14 s

CPU
---
Load Average: 0.29, 0.44, 0.44
CPU Count: 12

Memory
------
Used: 7.3 GiB / 30.5 GiB

Disk
----
/: 36.1% used
/home: 36.1% used
/boot: 32.1% used
/boot/efi: 3.3% used

Services
--------
Failed systemd units: 1
  example.service

Security
--------
SELinux: Enforcing
Firewalld: Active

Actual output will vary depending on the system.
