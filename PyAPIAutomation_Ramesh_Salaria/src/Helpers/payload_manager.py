from typing import Dict

def create_booking() -> Dict:
    return {
        "firstname": "Ramesh",
        "lastname": "Salaria",
        "totalprice": 112,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2018-01-01"
        },
        "additionalneeds": "Breakfast"
    }

def get_booking() -> Dict:
    return create_booking()

def patch_update() -> Dict:
    return {
        "firstname": "Ramesh",
        "lastname": "Salaria"
    }

def create_token() -> Dict:
    return {
        "username": "admin",
        "password": "password123"
    }
