import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if hours := re.search("(1?[0-9]):?([0-5]?[0-9]?) ([A|P]M) to (1?[0-9]):?([0-5]?[0-9]?) ([A|P]M)", s, re.IGNORECASE):
        start_hour, start_minute, start = hours.group(1), hours.group(2), hours.group(3)
        end_hour, end_minute, end = hours.group(4), hours.group(5), hours.group(6)

        if len(start_hour) == 1:
            start_hour = "0" + start_hour
        if len(end_hour) == 1:
            end_hour = "0" + end_hour

        if start.upper() == "PM":
            start_hour = int(start_hour)
            start_hour += 12
        if end.upper() == "PM":
            end_hour = int(end_hour)
            if end_hour != 12:
                end_hour += 12
        if start.upper() == "AM" and int(start_hour) == 12:
            start_hour = "00"

        if not start_minute:
            start_minute = "00"
        if not end_minute:
            end_minute = "00"

        return f"{start_hour}:{start_minute} to {end_hour}:{end_minute}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
