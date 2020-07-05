import pymysql as pymysql


def get_password_from_db(account):
    # dict = {
    #     "joey": "91",
    #     "mei": "99",
    # }
    #
    # return dict.get(account)
    try:
        conn = pymysql.connect(host='127.0.0.1', user='root', passwd="xxx", db='mysql')
        cur = conn.cursor()
        cur.execute("SELECT Password FROM user WHERE account = %s" % account)
        for r in cur:
            return r
    finally:
        cur.close()
        conn.close()
