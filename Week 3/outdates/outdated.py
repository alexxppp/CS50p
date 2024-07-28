months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}


def main():
    while True:
        date = input("date here: ")

        newdate = None
        if 11 <= len(date) <= 18 and ("," in date):
            newdate = convert_format2(date)
        elif 8 <= len(date) <= 10 and ("/" in date):
            newdate = convert_format1(date)

        if newdate:
            try:
                year, month, day = map(int, newdate.split("-"))
                if validate_date(year, month, day):
                    print(newdate)
                    break
            except ValueError:
                pass
        else:
            print("Invalid date format. Please try again.")


def convert_format1(date):
    date = date.strip().split("/")
    if len(date[0]) == 1:
        date[0] = f"0{date[0]}"
    if len(date[1]) == 1:
        date[1] = f"0{date[1]}"
    return f"{date[2]}-{date[0]}-{date[1]}"


def convert_format2(date):
    date = date.rstrip(",").split(" ")
    month_name = date[0].capitalize()
    if month_name in months:
        day = date[1].strip(',')
        if len(day) == 1:
            day = "0" + day
        return f"{date[2]}-{months[month_name]}-{day}"
    return None


def validate_date(year, month, day):
    if not (0 <= year <= 2024):
        return False
    if not (1 <= month <= 12):
        return False
    if not (1 <= day <= 31):
        return False
    return True


main()
