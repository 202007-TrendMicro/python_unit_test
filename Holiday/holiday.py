from datetime import date


def say_hello():
    today = __get_today()
    if today.strftime("%m/%d") == "12/25":
        return "Merry Xmas"
    return "Today is not Xmas"


def __get_today():
    return date.today()
