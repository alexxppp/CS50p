from datetime import date, timedelta
import sys
import inflect
import re
import operator


def main():
    print(get_minutes(input("Your birth date: ")))


def get_minutes(s):

    if not re.search(r"\d{4}-\d{2}-\d{2}", s):
        sys.exit(1)

    # Just because, this is the all-in-one line version (it actually works)
    return re.sub(r"\b and\b", "", inflect.engine().number_to_words(operator.__sub__(date.today(), date(int(s.split("-")[0]), int(s.split("-")[1]), int(s.split("-")[2]))).total_seconds() / 60)).capitalize().replace(" point zero", "") + " minutes"

    # Full version
    # year, month, day = s.split("-")
    # try:
    #     birth = date(int(year), int(month), int(day))
    # except ValueError:
    #     sys.exit(1)
    #
    # minutes = operator.__sub__(date.today(), birth).total_seconds() / 60
    # p = inflect.engine()
    # word = re.sub(r"\b and\b", "", p.number_to_words(minutes))

    # return word.capitalize().replace(" point zero", "") + " minutes"


if __name__ == "__main__":
    main()
