import http.client

URL = "api.fortnitetracker.com"
HEADERS = {"TRN-Api-Key": "76b3c847-e54a-45c6-8966-397f20eba36c"}
URL_FORMAT = "/v1/profile/pc/{}"


def flat(list_of_dicts):
    dict1 = {}
    for element in list_of_dicts:
        dict1[element.get("key")] = element.get("value")
    return dict1


def get_stats(*nickname):
    connection = http.client.HTTPSConnection(URL)
    url = URL_FORMAT.format(" ".join(nickname))
    connection.request("GET", url, headers=HEADERS)
    response = connection.getresponse()
    if response.code != 200:
        raise BadConnection()
    response_body = eval(response.read())
    if "error" in response_body.keys():
        raise InputException()
    lifetime_stats = flat(response_body.get("lifeTimeStats"))
    response_body = {key: lifetime_stats[key] for key in ('K/d', 'Win%', 'Wins', 'Kills', 'Matches Played')}
    return response_body


class InputException(Exception):
    pass


class BadConnection(Exception):
    pass
