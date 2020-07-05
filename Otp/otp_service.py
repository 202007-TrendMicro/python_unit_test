import random


def get_otp(account):
    return '{:06d}'.format(random.randint(0, 999999))
