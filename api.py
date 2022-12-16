import requests


def get_nobel_prize(year: int, field: str | None = None) -> dict:
    if field is None:
        parameters = {"nobelPrizeYear": year}
    else:
        parameters = {"nobelPrizeYear": year, "nobelPrizeCategory": field}
    res = requests.get(
        "http://api.nobelprize.org/2.1/nobelPrizes", params=parameters).json()
    return res
