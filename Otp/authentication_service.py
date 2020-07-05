from Otp.otp_service import get_otp
from Otp.profile_dao import get_password_from_db


def is_valid(account, password):
    password_from_db = get_password_from_db(account)
    otp = get_otp(account)

    print(otp)

    valid_password = password_from_db + otp
    if valid_password == password:
        return True
    else:
        return False
