import cpu
import disk
import memory
import system
import systemd


def main():
    systemd.get_failed_units()


if __name__ == "__main__":
    main()
