import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(:\d{2})?\s(AM|PM)\s+to\s+(\d{1,2})(:\d{2})?\s(AM|PM)$"
    if matches := re.search(pattern, str(s)):

        start_hour = int(matches.group(1))
        end_hour = int(matches.group(4))
        start_meridiem = matches.group(3)
        end_meridiem = matches.group(6)

        start_minute = matches.group(2)
        if start_minute:
            start_minute = int(start_minute[1:])
        else:
            start_minute = 0

        end_minute = matches.group(5)
        if end_minute:
            end_minute = int(end_minute[1:])
        else:
            end_minute = 0

        if start_meridiem == "PM" and start_hour <= 12:
            start_hour = (int(start_hour) + 12) % 24
        if end_meridiem == "PM" and end_hour <= 12:
            end_hour = (int(end_hour) + 12) % 24
    
        if 0 <= start_hour <= 23 and 0 <= start_minute < 60 and 0 <= end_hour <= 23 and 0 <= end_minute < 60:
            return f"{start_hour:02d}:{start_minute:02d} to {end_hour:02d}:{end_minute:02d}"

    raise ValueError("Invalid time format or invalid time values")



if __name__ == "__main__":
    main()