from random import randint
from time import time
import requests


def r_num():
    r1 = randint(-10, 10)
    print(r1)
    return r1


def get_random_expiration_date():
    milliseconds = int(round(time() * 1000))  # current time
    day_in_millis = 1000 * 60 * 60 * 24

    r_exp_date: int
    if r_num() < 0:
        r_exp_date = milliseconds - abs(day_in_millis)
    else:
        r_exp_date = milliseconds + day_in_millis

    return r_exp_date


def create_mockup():
    url = 'https://61eb3ca87ec58900177cdbe1.mockapi.io/api/v1/repository/commidity'

    for i in range(87, 101):
        myObj = {
            "name": f"Food ${i}",
            "category": "Food",
            "expiryDate": int(get_random_expiration_date()),
            "mId": i
        }

        x = requests.post(url, data=myObj)
        print(x.text)


if __name__ == '__main__':
    create_mockup()
