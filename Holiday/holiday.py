from datetime import date


def say_hello():
    today = date.today()
    if today.strftime("%m/%d") == "12/25":
        return "Merry Xmas"
    return "Today is not Xmas"
