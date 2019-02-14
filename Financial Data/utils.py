from datetime import datetime


def convert_to_hour(date):
    new_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    return new_date.hour

def convert_to_date(date):
    new_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    return new_date.date()
