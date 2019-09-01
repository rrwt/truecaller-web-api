import os
from typing import Tuple

import requests
import json

API_KEY: str = os.getenv("API_KEY")

if not API_KEY:
    raise AssertionError("API KEY NOT FOUND")


def fetch_request_id(phone_number: str) -> Tuple[int, str]:
    url: str = "https://api4.truecaller.com/v1/apps/requests"
    headers: dict = {"content-type": "application/json", "appkey": API_KEY}

    response = requests.post(
        url, headers=headers, data=json.dumps({"phoneNumber": phone_number})
    )

    if response.status_code == 200:
        return 200, json.loads(response.text)["requestId"]
    else:
        return response.status_code, json.loads(response.content)['message']


def fetch_user_information(access_token: str) -> dict:
    url: str = "https://profile4.truecaller.com/v1/default"
    headers: dict = {'content-type': 'application/json', 'Authorization': 'Bearer ' + access_token}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)

    if data['status'] == 200:
        data['has_table_data'] = True
        return data
    else:

        return data
