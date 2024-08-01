import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if correct := re.search(r"^([0-9]*)\.([0-9]*)\.([0-9]*)\.([0-9]*)$", ip):
        if 0 <= int(correct.group(1)) <= 255 and 0 <= int(correct.group(2)) <= 255 and 0 <= int(correct.group(3)) <= 255 and 0 <= int(correct.group(4)) <= 255:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
