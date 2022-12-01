from os import environ
from pathlib import Path

import requests


def get_full_text(path: str):
    with open(path, "r") as f:
        output = f.read()
    return output


def full_text_to_list(text: str, element_type=str):
    output = text.split("\n")
    if element_type is not str:
        output = [element_type(i) for i in output]
    return output


def download_input(year, day):
    resp = requests.get(
        f'https://adventofcode.com/{year}/day/{day}/input',
        cookies={
            'session': environ['AOC_TOKEN']
        },
        headers={
            'User-Agent': 'Python Via rinejames@gmail.com'
        }
    )
    if resp.status_code != 200:
        raise requests.HTTPError(f"Could Not get data for {year}/{day}")

    return resp.content.decode()


def year_and_date(file_path):
    path = Path(file_path)
    day = path.parent
    year = day.parent
    return year.name, day.name
